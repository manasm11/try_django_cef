from django.urls import include, path
from test1 import views

urlpatterns = [
    path('', views.create_test_view, "test1_create.html"),
]
