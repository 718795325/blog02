"""
Django settings for Django_Projects project.

Generated by 'django-admin startproject' using Django 2.2.

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
SECRET_KEY = 'apwgii24xz&%9bh36^trkv$v=2957_=zyz#0z_9b+-g09z1r+^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App.apps.AppConfig',
    # 'tinymce',
    'captcha',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'App.MyMiddleware.MyMiddleware',

]

ROOT_URLCONF = 'Django_Projects.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': False,
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

WSGI_APPLICATION = 'Django_Projects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog03',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PASSWORD': '123456',
        'POST': 3306,
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
#表单验证注册
AUTH_USER_MODEL = 'App.User'
#文件上传路径
# MDEIA_ROOT = os.path.join(BASE_DIR,'static/filesss')

#验证码
# CAPTCHA_IMAGESIZE = (30,60)   # 设置captcha图片大小
#
# CAPTCHA_LENGTH =4   #字符个数
# CAPTCHA_TIMEOUT =1  #超时(minutes)*
#
# # 输出格式：输入框验证码图片隐藏域•
# # '%(image)s %(hidden_field)s %(text_field)s'
# CAPTCHA_OUTPUT_FORMAT ='%(text_field)s %(image)s %(hidden_field)s'
# CAPTCHA_NOISE_FUNCTIONS =(
#     'captcha.helpers.noise_null',
#     'captcha.helpers.noise_arcs',
#     'captcha.helpers.noise_dots',
# )
# CAPTCHA_CHALLENGE_FUNCT =  'captcha.helpers.math_challenge'

#邮件发送
EMAIL_HOST = 'smtp.qq.com'
# EMAIL_PORT = 25
EMAIL_HOST_USER = '2458824779@qq.com'
EMAIL_HOST_PASSWORD = 'udoampbpsgyseaec'
EMAIL_USE_TLS = True
# #收件⼈看到的发件⼈ <此处要和发送邮件的邮箱相同>
EMAIL_FROM = 'sky<2458824779@qq.com>'
