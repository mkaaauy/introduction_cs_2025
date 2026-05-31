from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="image_url",
            field=models.URLField(blank=True, max_length=1000, verbose_name="Изображение"),
        ),
    ]
