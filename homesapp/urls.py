from django.conf.urls import url,include
from django.contrib import admin
from .import views

urlpatterns = [
    #/homesapp/
    url(r'^$', views.IndexView.as_view(),name='index'),
    #/homesapp/1
    url(r'^(?P<pk>[0-9]+)/$', views.LocationView.as_view(),name='property'),
    #/homesapp/1/2
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/$',views.PropertyDetail.as_view(),name='propertyview'),
]
