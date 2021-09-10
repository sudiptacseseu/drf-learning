from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


# Concrete api view (Separate view)
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # Static filtering
    # queryset = Student.objects.filter(passby='user')
    serializer_class = StudentSerializer

    # Set filter locally using django filter backend
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    # filterset_fields = ['name', 'city']

    # Set filter using search filter
    # filter_backends = [SearchFilter]
    # search_fields = ['name', 'city']
    # Starts with
    # search_fields = ['^name']
    # Exact match
    # search_fields = ['=name']
    # Full text search(only supports on PostGreSQL
    # search_fields = ['@name']

    # Set filter using ordering filter
    filter_backends = [OrderingFilter]
    # ordering_fields = ['name']
    ordering_fields = ['name', 'city']

    # Filter by current user
    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# For CRUD only ListCreate and RetrieveUpdateDestroy are enough
# List and create - pk is not required
# class ListCreateStudent(ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# # Retrieve and update - pk is required
# class RetrieveUpdateStudent(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# # Retrieve and destroy - pk is required
# class RetrieveDestroyStudent(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# # Retrieve, update and delete - pk is required
# class RetrieveUpdateDestroyStudent(RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
