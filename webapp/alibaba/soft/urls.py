from django.conf.urls import patterns, url, include

urlpatterns = [
    url(r'^$', "soft.views.index", name='soft_home'),
]