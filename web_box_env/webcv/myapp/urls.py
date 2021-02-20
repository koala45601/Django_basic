from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('hello/<str:id>', views.hello,name='hello1'),
    re_path(r're_path/$', views.re_path,name='repath1'),
    re_path(r're_path_2/(?P<year>[0-9]{4})/$', views.re_path_2,name='repath2'),
    re_path(r're_path_3/(?P<ID_2>[0-9]{4})/(?P<slug>[\w-]+)/$', views.re_path_3,name='repath3'),

]