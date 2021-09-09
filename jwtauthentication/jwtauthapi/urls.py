from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating router object
router = DefaultRouter()

# Register StudentViewSet with router
router.register('student-api', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),

    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify-token/', TokenVerifyView.as_view(), name='token_verify'),

]