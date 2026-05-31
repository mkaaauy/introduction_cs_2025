from django.core.management.base import BaseCommand

from news.services import fetch_all_active_feeds


class Command(BaseCommand):
    help = "Загрузить новости из RSS"

    def handle(self, *args, **options):
        results = fetch_all_active_feeds()
        for name, count in results.items():
            if count >= 0:
                self.stdout.write(f"{name}: +{count}")
            else:
                self.stdout.write(self.style.ERROR(f"{name}: ошибка"))
