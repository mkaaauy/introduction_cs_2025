from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_article_image_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedsource",
            name="lang",
            field=models.CharField(
                choices=[("ru", "Русский"), ("en", "English")],
                default="ru",
                max_length=2,
                verbose_name="Язык ленты",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="is_translated",
            field=models.BooleanField(default=False, verbose_name="Переведено"),
        ),
        migrations.AddField(
            model_name="article",
            name="title_original",
            field=models.CharField(blank=True, max_length=500, verbose_name="Заголовок (ориг.)"),
        ),
        migrations.AddField(
            model_name="article",
            name="summary_original",
            field=models.TextField(blank=True, verbose_name="Описание (ориг.)"),
        ),
    ]
