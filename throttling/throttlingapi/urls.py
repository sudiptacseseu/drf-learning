from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating router object
router = DefaultRouter()

# Register StudentViewSet with router
router.register('student-api', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),

    # To enable login dialog on session authentication
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))

]
