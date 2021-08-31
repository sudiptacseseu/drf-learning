from django.urls import path
from . import views

urlpatterns = [
    path('student-info/', views.student_list),
    path('student-info/<int:pk>', views.student_detail)
]
