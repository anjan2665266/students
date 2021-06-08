from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import adminfunctions

urlpatterns = [
    url(r'^processfile/(?P<file_type>[\w\-]+)/(?P<pk>.*)/$',adminfunctions.ProcessFiles.as_view(),name ='processfile'),
    url(r'^processfile/(?P<file_type>[\w\-]+)/$', adminfunctions.ProcessFiles.as_view(),name ='processfile'), 
]