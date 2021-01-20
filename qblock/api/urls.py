from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
        path('', views.api_overview, name='home'),
        path('users_list/', views.users_list, name='users_list'),
        path('user/<str:pk>/', views.user, name='user'),

]
