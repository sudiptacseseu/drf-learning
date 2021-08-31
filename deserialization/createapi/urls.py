from django.urls import path
from . import views

urlpatterns = [
    path('student-create/', views.student_create),
]
