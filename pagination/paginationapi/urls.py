from django.urls import path
from . import views

urlpatterns = [

    path('student-api/', views.StudentList.as_view()),
]
