from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /article/[article_id]
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article, name='article'),
]
