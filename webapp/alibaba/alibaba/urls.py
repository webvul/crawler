# coding=utf-8
"""crawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^wanglingling/', include(admin.site.urls)),
    url(r'^$', "alibaba.views.index", name='alibaba_home'),
    url(r'^search/',  "alibaba.views.search", name='alibaba_search'),
    url(r'^ask/',  "ask.views.index", name='ask_home'),
    url(r'^git/',  "git.views.index", name='git_home'),
    url(r'^doc/',  "doc.views.index", name='doc_home'),
    url(r'^code/',  "code.views.index", name='code_home'),
    url(r'^library/',  "library.views.index", name='library_home'),
    url(r'^news/',  "news.views.index", name='news_home'),
    url(r'^soft/',  "soft.views.index", name='soft_home'),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^accounts/', include('userena.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^captcha/', include('captcha.urls')),

]

urlpatterns += patterns('', url(r'^silk/', include('silk.urls', namespace='silk')))

urlpatterns += patterns('', url(r'', include('social_auth.urls')))

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
