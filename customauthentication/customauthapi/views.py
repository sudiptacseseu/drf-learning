from django.shortcuts import render
from rest_framework import viewsets

from .customauth import CustomAuthentication
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
