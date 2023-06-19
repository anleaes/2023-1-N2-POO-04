from django.shortcuts import render
from .models import App
from rest_framework import viewsets
from .serializer import AppSerializer

# Create your views here.

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer