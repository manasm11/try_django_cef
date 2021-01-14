from django.urls import path, include
from .views import home_view
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

router = DefaultRouter()
router.register('profiles', UserProfileViewSet)

urlpatterns = [
    path('', home_view),
    path('', include(router.urls)),
]
