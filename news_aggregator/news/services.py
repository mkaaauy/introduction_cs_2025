from datetime import datetime, timezone as dt_timezone
import html
import re
import socket
import time

import feedparser
from django.conf import settings
from django.utils import timezone
from django.utils.html import strip_tags

from .models import Article, FeedSource


def ensure_default_sources():
    for item in settings.DEFAULT_FEED_SOURCES:
        FeedSource.objects.update_or_create(
            url=item["url"],
            defaults={
                "name": item["name"],
                "is_active": True,
                "lang": item.get("lang", "ru"),
            },
        )


def _parse_feed(url):
    timeout = getattr(settings, "FEED_FETCH_TIMEOUT", 15)
    old = socket.getdefaulttimeout()
    socket.setdefaulttimeout(timeout)
    try:
        return feedparser.parse(url, agent="Mozilla/5.0")
    finally:
        socket.setdefaulttimeout(old)


def _parse_published(entry):
    for attr in ("published_parsed", "updated_parsed"):
        parsed = getattr(entry, attr, None)
        if parsed:
            return datetime(*parsed[:6], tzinfo=dt_timezone.utc)
    return None


def _clean_text(raw, limit=None):
    text = html.unescape(strip_tags(raw or "")).strip()
    if limit:
        return text[:limit]
    return text


def _extract_image(entry):
    if getattr(entry, "media_thumbnail", None):
        url = entry.media_thumbnail[0].get("url")
        if url:
            return url[:1000]

    raw = entry.get("summary") or entry.get("description") or ""
    match = re.search(r"""<img[^>]+src=["']([^"']+)["']""", raw, re.I)
    if match:
        return match.group(1)[:1000]
    return ""


def _translate(text):
    if not text:
        return text
    try:
        from deep_translator import GoogleTranslator

        return GoogleTranslator(source="en", target="ru").translate(text)
    except Exception:
        return text


def fetch_feed(source):
    parsed = _parse_feed(source.url)
    if parsed.bozo and not parsed.entries:
        raise ValueError(parsed.bozo_exception)

    new_count = 0
    for entry in parsed.entries:
        link = entry.get("link")
        title = _clean_text(entry.get("title"), 500)
        summary = _clean_text(entry.get("summary") or entry.get("description"), 500)
        if not link or not title:
            continue

        if source.lang == "en" and settings.AUTO_TRANSLATE_TO_RU:
            title = _translate(title)
            if summary:
                summary = _translate(summary)
                time.sleep(0.1)

        article, created = Article.objects.get_or_create(
            link=link,
            defaults={
                "source": source,
                "title": title[:500],
                "summary": summary,
                "image_url": _extract_image(entry),
                "published_at": _parse_published(entry),
            },
        )
        if created:
            new_count += 1
        elif not article.image_url:
            article.image_url = _extract_image(entry)
            article.save(update_fields=["image_url"])

    source.last_fetched_at = timezone.now()
    source.save(update_fields=["last_fetched_at"])
    return new_count


def fetch_all_active_feeds():
    ensure_default_sources()
    results = {}
    for source in FeedSource.objects.filter(is_active=True):
        try:
            results[source.name] = fetch_feed(source)
        except Exception:
            results[source.name] = -1
    return results
