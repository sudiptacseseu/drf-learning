from django.urls import path
from . import views

urlpatterns = [
    path('student-api/', views.StudentAPI.as_view()),
    path('student-api/<int:pk>', views.StudentAPI.as_view()),
]
