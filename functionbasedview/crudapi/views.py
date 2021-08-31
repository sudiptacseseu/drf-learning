import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_api(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Data created!'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    elif request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            # json_data = JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(serializer.data)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        # partial=False means user need to give full data otherwise it will show required field error
        serializer = StudentSerializer(student, data=python_data, partial=False)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Data updated!'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer.render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    elif request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        student = Student.objects.get(id=id)
        student.delete()

        response = {'message': 'Data deleted!'}
        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data, content_type='application/json')


