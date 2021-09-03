from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


# @api_view()
# def hello_world(request):
#     return Response({'message': 'Hello world'})


# @api_view(['GET'])
# def hello_world(request):
#     return Response({'message': 'Hello world'})


# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'message': 'This is post request'})


# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == "GET":
#         print(request.data)
#         return Response({'message': 'This is get request'})
#     if request.method == "POST":
#         print(request.data)
#         return Response({'message': 'This is post request', 'data': request.data})


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == "GET":
        # If pk sent by data from third party
        # pk = request.data.get('id')
        if pk is not None:
            student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data created!'}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Full data updated!'})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Partial data updated!'})
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        student = Student.objects.get(id=pk)
        student.delete()
        return Response({'message': 'Data deleted!'})
