from django.urls import path, include
from . import views
urlpatterns = [
    path('home/', views.StudentAPI.as_view(), name='home'),
    path('home/<int:id>/', views.StudentAPI.as_view(), name='home'),

]