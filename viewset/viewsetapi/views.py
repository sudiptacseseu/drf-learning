from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        print("**List**")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if pk is not None:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data created!'}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Full data updated!'})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Partial data updated!'})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'message': 'Data deleted!'})
