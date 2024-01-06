from django.shortcuts import render
from rest_framework.response import Response
from.models import *
from.serializers import *
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
class Studentviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUser]


