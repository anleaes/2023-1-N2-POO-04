from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'app'

router = routers.DefaultRouter()
router.register('app', views.AppViewSet, basename = 'app')

urlpatterns = [
    path('', include(router.urls) )
]