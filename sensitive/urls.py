from django.conf.urls import url

from . import views

app_name = 'sensitive'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/detail/$', views.detail, name='detail'),
]