from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'revenue'

router = routers.DefaultRouter()
router.register('revenue', views.RevenueViewSet, basename='revenue')

urlpatterns = [
    path('', include(router.urls) )
]
