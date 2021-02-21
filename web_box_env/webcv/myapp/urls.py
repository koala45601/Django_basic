from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    #localhost:8000/
    path('', views.hello_homepage,name='index_1'),
    #localhost:8000/hello/(ใส่เลขในตัวแปร id)
    path('hello/<str:id>', views.hello,name='hello1'),
    #localhost:8000/re_path/
    re_path(r're_path/$', views.re_path,name='repath1'),
    #localhost:8000/re_path/(ใส่เลข4ตัว ตัวแปรคือ year)
    re_path(r're_path_2/(?P<year>[0-9]{4})/$', views.re_path_2,name='repath2'),
    #localhost:8000/re_path/(ใส่เลข4 ตัว ตัวแปร year และใส่่สลัก(-)เช่น Petong-miss)
    re_path(r're_path_3/(?P<ID_2>[0-9]{4})/(?P<slug>[\w-]+)/$', views.re_path_3,name='repath3'),
    #localhost:8000/hello_hompage
    #path('hello_homepage/', views.hello_homepage,name= 'home1')

]