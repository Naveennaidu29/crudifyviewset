from django.shortcuts import render
from rest_framework.response import Response
from.models import *
from.serializers import *
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

# Create your views here.
class Studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


