from django.shortcuts import render
from .models import Revenue
from rest_framework import viewsets
from .serializer import RevenueSerializer

# Create your views here.

class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
