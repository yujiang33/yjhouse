"""
Django settings for demo3 project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8wyy5mj%j&d84+lx+^_flcobyp%m1q(l1h&@qcad+8a6qr2j+9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
#新建完应用后,将他们配置在这里
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'comments',
    'tinymce',    #将富文本注册这 注册应用，可以找到应用下文件夹
    'haystack',
]
#中间件  扩展通用(每一次请求)功能
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo3.urls'
# 配置模板,新建模板将模板配置在这里
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"template")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# 配置中文
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE='zh-hans'
# 配置时区
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/ShangHai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# 配置 动态文件
STATIC_URL = '/static/'
STATICFILES_DIRS =[os.path.join(BASE_DIR,"static")]
# 配置轮播图,,在static下新建media文件夹,将图片储存下来,数据库储存图片路径
MEDIA_ROOT= os.path.join(BASE_DIR,'static/media')

#需要安装pip install django-tinymce 然后富文本配置项目,非富多彩的文本,
TINYMCE_DEFAULT_CONFIG={
    'theme':'advanced',
    'width':600,
    'heigth':400,
}



# 邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True #是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = False #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.163.com' #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 25 #发件箱的SMTP服务器端口
EMAIL_HOST_USER = '18137128152@163.com' #发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'qikuedu'
DEFAULT_FROM_EMAIL = 'zzy0371 <18137128152@163.com>'


#使用redis缓存配置
CACHES={
    "default":{
        "BACKEND":"redis_cache.cache.RedisCache",
        "LOCATION":"localhost:6379",
        "TIMEOUT":5,    #默认时间，以秒为单位
    },
}


#配置搜素信息

HAYSTACK_CONNECTIONS={
    'default':{
        'ENGINE':'blog.whoosh_cn_backend.WhooshEngine',
        'PATH':os.path.join(BASE_DIR,'whoosh_index'),
    }
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE=10
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'