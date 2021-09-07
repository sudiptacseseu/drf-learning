from django.shortcuts import render
from rest_framework import viewsets

from .custompermissions import MyCustomPermission
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyCustomPermission]
