from usuarios.views import index, login, cadastro, logout
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
]