import os
import sys
import threading
import time

from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "news"

    def ready(self):
        from django.conf import settings

        if not settings.AUTO_FETCH_FEEDS:
            return
        if "runserver" not in sys.argv:
            return
        if os.environ.get("RUN_MAIN") != "true" and "--noreload" not in sys.argv:
            return

        def update_feeds():
            while True:
                time.sleep(settings.FEED_FETCH_INTERVAL_MINUTES * 60)
                from news.services import fetch_all_active_feeds

                fetch_all_active_feeds()

        threading.Thread(target=update_feeds, daemon=True).start()
