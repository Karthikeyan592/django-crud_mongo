from django.urls import path
from crud import views
#from django.conf.urls import url
from django.urls import re_path

urlpatterns=[
    # url(r'^crud$',views.userApi),
    # url(r'^crud/([0-9]+)$',views.userApi),
    re_path(r'^crud$', views.userApi),
    re_path(r'^crud/([0-9]+)$', views.userApi),
   

]

