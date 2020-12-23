from django.urls import path
from test3 import views

urlpatterns = [
    path('', views.create_view),
]
