from django.contrib import admin
from django.urls import path,include
from testing import views
from django.conf import settings

urlpatterns = [
   path('',views. index,name='index'),
   
]
