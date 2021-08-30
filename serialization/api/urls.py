from django.urls import path
from api import views

urlpatterns = [
    path('student_info/', views.student_list),
    path('student_info/<int:pk>', views.student_detail)
]
