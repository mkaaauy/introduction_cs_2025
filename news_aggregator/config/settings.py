from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-dev-key"

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "news.apps.NewsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Europe/Moscow"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_FEED_SOURCES = [
    {"name": "Playground", "url": "https://www.playground.ru/rss/news.xml", "lang": "ru"},
    {"name": "DTF", "url": "https://dtf.ru/rss/all", "lang": "ru"},
    {"name": "Игромания", "url": "https://www.igromania.ru/rss/news.xml", "lang": "ru"},
    {"name": "Habr — Игры", "url": "https://habr.com/ru/rss/hubs/games/articles/all/", "lang": "ru"},
    {"name": "GameSpot", "url": "https://www.gamespot.com/feeds/news/", "lang": "en"},
    {"name": "PC Gamer", "url": "https://www.pcgamer.com/rss/", "lang": "en"},
    {"name": "Rock Paper Shotgun", "url": "https://www.rockpapershotgun.com/feed", "lang": "en"},
    {"name": "3DNews", "url": "https://3dnews.ru/news/rss/", "lang": "ru"},
    {"name": "Overclockers", "url": "https://overclockers.ru/rss/news.rss", "lang": "ru"},
    {"name": "Habr — Железо", "url": "https://habr.com/ru/rss/hubs/hardware/articles/all/", "lang": "ru"},
    {"name": "Tom's Hardware", "url": "https://www.tomshardware.com/feeds/all", "lang": "en"},
    {"name": "TechPowerUp", "url": "https://www.techpowerup.com/rss/news", "lang": "en"},
    {"name": "Neowin — Драйверы", "url": "https://www.neowin.net/news/rss/tags/drivers/", "lang": "en"},
]

AUTO_FETCH_FEEDS = True
FEED_FETCH_INTERVAL_MINUTES = 30
ARTICLES_PER_PAGE = 20
FEED_FETCH_TIMEOUT = 15
AUTO_TRANSLATE_TO_RU = True
