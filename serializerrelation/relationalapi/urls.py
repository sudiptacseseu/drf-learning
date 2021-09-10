from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating router object
router = DefaultRouter()

# Register StudentViewSet with router
router.register('singer', views.SingerModelViewSet, basename='singer')
router.register('song', views.SongModelViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls))

]
