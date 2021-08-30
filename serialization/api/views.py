from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Model object - Single student data
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)


# Queryset - All student data
def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')



