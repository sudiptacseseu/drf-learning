from django.urls import path
from . import views

urlpatterns = [
    path('student-api/', views.student_api),
    path('student-api/<int:pk>', views.student_api),
]
