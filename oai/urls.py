from django.conf.urls import url

from . import views


app_name = 'oai'
urlpatterns = [
    url(r'^(.+?)/xml/$', views.xml, name='xml'),
    url(r'^(.+?)/thumbnail/$', views.thumbnail, name='thumbnail'),    
    url(r'^harvest/$', views.harvest, name='harvest'),
    url(r'^$', views.index, name='index'),
]