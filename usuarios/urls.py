from usuarios.views import login, cadastro, logout
from django.urls import path

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
]