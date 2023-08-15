from django.urls import path
from . import views

urlpatterns = [
    path('config', views.config_env_file, name='index'),
]
