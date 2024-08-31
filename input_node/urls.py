from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_node, name='input_node'),
]