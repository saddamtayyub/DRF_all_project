from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.student_api, name='home'),
    path('home/<int:id>/', views.student_api, name='home'),

]