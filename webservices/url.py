from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import adminfunctions

urlpatterns = [
    url(r'^studentmarks/$', adminfunctions.StudentMarks.as_view(),name ='studentmarks'),
    url(r'^studentmarks/(?P<pk>[0-9]+)/$', adminfunctions.StudentMarks.as_view(),name ='studentmarks'),
    url(r'^totalmarks/$', adminfunctions.TotalMarks.as_view(),name ='totalmarks'),
    url(r'^averagemarks/$', adminfunctions.AverageMarks.as_view(),name ='averagemarks'),
]