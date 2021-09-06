from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Set authentication and permission locally(view wise) - it can override the declaration set globally if there any
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # Multiple permissions can be added
    # permission_classes = [IsAuthenticated, IsAdminUser]
