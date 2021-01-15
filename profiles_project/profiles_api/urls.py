from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profiles', views.UserViewSet)
router.register('feeds', views.FeedViewSet)

urlpatterns = [
    path('', views.home_view),
    path('login/', views.UserLoginView.as_view()),
    path('', include(router.urls)),

]
