from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .auth import CustomAuthToken

# Creating router object
router = DefaultRouter()

# Register StudentViewSet with router
router.register('student-api', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),

    # To enable login dialog on session authentication
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    # To get token for an user(default response)
    # path('obtain-token/', obtain_auth_token),

    # To get token for an user(custom response with user details)
    path('obtain-token/', CustomAuthToken.as_view())

]
