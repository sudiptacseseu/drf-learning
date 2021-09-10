from django.urls import path
from . import views

urlpatterns = [

    # For separate call
    # path('student-api/', views.StudentList.as_view()),
    # path('student-api/', views.StudentCreate.as_view()),
    path('student-api/<int:pk>', views.StudentRetrieve.as_view()),
    # path('student-api/<int:pk>', views.StudentDestroy.as_view()),

    # For combined call
    # path('student-api/', views.ListCreateStudent.as_view()),
    # path('student-api/<int:pk>', views.RetrieveUpdateStudent.as_view()),
    # path('student-api/<int:pk>', views.RetrieveDestroyStudent.as_view()),
    # path('student-api/<int:pk>', views.RetrieveUpdateDestroyStudent.as_view()),
]
