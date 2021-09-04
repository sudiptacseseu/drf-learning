from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


class StudentAPI(APIView):
    @staticmethod
    def get(request, pk=None, format=None):
        if pk is not None:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data created!'}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, pk=None, format=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Full data updated!'})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def patch(request, pk=None, format=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Partial data updated!'})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk=None, format=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'message': 'Data deleted!'})
