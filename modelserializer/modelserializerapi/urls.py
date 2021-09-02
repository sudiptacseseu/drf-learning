from django.urls import path
from . import views

urlpatterns = [
    path('student-api/', views.StudentApi.as_view()),
]
