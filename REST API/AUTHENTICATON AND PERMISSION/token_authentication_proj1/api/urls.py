from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('studentapi', views.StudentModelViewSet, basename='Studentapi')

urlpatterns = [

    path('', include(router.urls)),
    path('gettoken/', obtain_auth_token),

]