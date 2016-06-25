from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.contact_page, name='contact_page.html')
]
