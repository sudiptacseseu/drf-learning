from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer


# Concrete api view (Separate view)
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# For CRUD only ListCreate and RetrieveUpdateDestroy are enough
# List and create - pk is not required
class ListCreateStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Retrieve and update - pk is required
class RetrieveUpdateStudent(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Retrieve and destroy - pk is required
class RetrieveDestroyStudent(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Retrieve, update and delete - pk is required
class RetrieveUpdateDestroyStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
