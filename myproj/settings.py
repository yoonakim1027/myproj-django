"""
Django settings for myproj project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from datetime import timedelta
from environ import Env  # 환경변수를 쉽게 변환

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = Env()

dot_env_path = BASE_DIR / ".env"
if dot_env_path.exists():
    with dot_env_path.open(encoding="utf-8") as f:
        env.read_env(f, overwrite=True)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 이 시크릿 키는? 매번 바뀔 수 있음
# 시크릿키는 암호화가 필요할 때 필요!
# 암호화(예를들어 패스워드) 할때, 이를 활용해서 암호화
# 단순 문자열인 SECRET_KEY는 변환이 필요가 없음~
SECRET_KEY = env.str("SECRET_KEY", default="---- SECRET KEY ----")
# 이렇게 하면? 이 이름의 환경변수를 문자열로 읽어서 대입해주게 됨
# 숫자라고 하면 env.int / 리스트면 env.list ~
# 환경변수가 없다면? 장고는 서버 구동이 안되고, 이 시점에서 키 에러가 난다.


# SECURITY WARNING: don't run with debug turned on in production!
# 이거는 True면 안돼 ~!
# 로컬에서 개발할때는 True / 운영할때는 False
DEBUG = env.bool('DEBUG', default=False)
# 서버에서 운영할때 DEBUG 옵션을 빼먹을 수도 있음
# 그렇더라도 기본으로는 False로 들어가야 함


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Application definition

INSTALLED_APPS = [
    # dajngo apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    # local apps
    "shop",
    "blog",
    "news",
    "youtubemusic",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myproj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myproj.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    #     #1줄의 환경변수로 셋팅! 장고가 제공~
    #
    # }

    # sqlite 파일경로를 db경로에 쓰고~ 이를 f스트링 문법으로 적용
    'default': env.db(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
    # 이 자체가 DATABASE_URL 환경변수를 파싱하여 dict 객체를 생성해준다!

}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = "/static/"
# 각 앱에 나눠서 저장된 static 파일들을 한 곳으로 저장할 디렉토리 경로
# 배포시에만 의미있는 설정
# 한 곳으로 모으는 명령 : python manage.py collectstatic
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# django-cors-headers
# https://github.com/adamchainz/django-cors-headers

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS",
                                default=['http://localhost:3000'])

# djangorestframework

# 인증을 지원하는 방법으로서 뭘쓸거야 ? Session방법이랑 authentication방법을 쓸거야

# 환경변수 설정 (DAYs니까 숫자! )-> env.int로 정수형으로 바꿔야 함
# 운영하다가도 정책이 바뀔 수 있음
ACCESS_TOKEN_LIFETIME_DAYS = env.int("ACCESS_TOKEN_LIFETIME_DAYS", default=0)
ACCESS_TOKEN_LIFETIME_HOURS = env.int("ACCESS_TOKEN_LIFETIME_HOURS", default=0)
ACCESS_TOKEN_LIFETIME_MINUTES = env.int("ACCESS_TOKEN_LIFETIME_MINUTES", default=5)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",

    ],

    # 원래 디폴트 만료 시간: 5분
    # 이렇게 위에 import 한 다음에 이렇게쓰면 ?
    # 새로 생성되는 토큰의 만료시간은 7일 뒤 !!
    'ACCESS_TOKEN_LIFETIME': timedelta(
        days=ACCESS_TOKEN_LIFETIME_DAYS,
        hours=ACCESS_TOKEN_LIFETIME_HOURS,
        minutes=ACCESS_TOKEN_LIFETIME_MINUTES,

    )

}
