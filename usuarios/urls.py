from usuarios.views import index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
]