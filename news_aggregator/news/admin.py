from django.contrib import admin

from .models import Article, FeedSource


@admin.register(FeedSource)
class FeedSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "last_fetched_at")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "source", "published_at")
    list_filter = ("source",)
    search_fields = ("title",)
