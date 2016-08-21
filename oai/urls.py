from django.conf.urls import url

from . import views


app_name = 'oai'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]