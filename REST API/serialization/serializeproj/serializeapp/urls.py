from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('home/<int:id>/', views.emp_details_serialized, name='home'),
    path('home/', views.emp_list_details_serialized, name='emplist'),

]