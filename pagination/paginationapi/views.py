from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .paginations import CustomPageNumberPagination
from .paginations import CustomLimitOffsetPagination
from .serializers import StudentSerializer


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # For page number pagination
    # pagination_class = CustomPageNumberPagination
    # For limit offset pagination
    pagination_class = CustomLimitOffsetPagination
