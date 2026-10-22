from usuarios.views import index, login, cadastrar, logout
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('logout', logout, name='logout'),
]