from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Article, FeedSource
from .services import fetch_all_active_feeds


def article_list(request):
    query = request.GET.get("q", "").strip()
    source_id = request.GET.get("source")
    period = request.GET.get("period", "")

    articles = Article.objects.select_related("source")

    if query:
        articles = articles.filter(
            Q(title__icontains=query) | Q(summary__icontains=query)
        )
    if source_id:
        articles = articles.filter(source_id=source_id)

    if period == "today":
        start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        articles = articles.filter(
            Q(published_at__gte=start)
            | Q(published_at__isnull=True, created_at__gte=start)
        )
    elif period == "week":
        start = timezone.now() - timedelta(days=7)
        articles = articles.filter(
            Q(published_at__gte=start)
            | Q(published_at__isnull=True, created_at__gte=start)
        )
    elif period == "month":
        start = timezone.now() - timedelta(days=30)
        articles = articles.filter(
            Q(published_at__gte=start)
            | Q(published_at__isnull=True, created_at__gte=start)
        )

    page_obj = Paginator(articles, settings.ARTICLES_PER_PAGE).get_page(
        request.GET.get("page")
    )

    params = request.GET.copy()
    params.pop("page", None)

    return render(
        request,
        "news/list.html",
        {
            "page_obj": page_obj,
            "articles": page_obj.object_list,
            "sources": FeedSource.objects.filter(is_active=True),
            "query": query,
            "selected_source": source_id or "",
            "selected_period": period,
            "period_choices": [
                ("", "Все время"),
                ("today", "Сегодня"),
                ("week", "Неделя"),
                ("month", "Месяц"),
            ],
            "query_string": params.urlencode(),
        },
    )


@require_POST
def refresh_feeds(request):
    results = fetch_all_active_feeds()
    total_new = sum(n for n in results.values() if n > 0)
    failed = [name for name, n in results.items() if n < 0]

    if total_new:
        messages.success(request, f"Добавлено новых статей: {total_new}")
    elif not failed:
        messages.info(request, "Новых статей нет")
    if failed:
        messages.warning(request, "Ошибка загрузки: " + ", ".join(failed))

    return redirect("article_list")
