from django.db import models


class FeedSource(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    lang = models.CharField(max_length=2, default="ru")
    is_active = models.BooleanField(default=True)
    last_fetched_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    source = models.ForeignKey(FeedSource, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=500)
    link = models.URLField(unique=True)
    summary = models.TextField(blank=True)
    image_url = models.URLField(max_length=1000, blank=True)
    published_at = models.DateTimeField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title_original = models.CharField(max_length=500, blank=True)
    summary_original = models.TextField(blank=True)
    is_translated = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title
