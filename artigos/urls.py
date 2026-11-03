from artigos.views import index, editor, redacao, publicar_artigo
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('redacao', redacao, name='redacao'),
    path('redacao/publicar/<int:id>/', publicar_artigo, name='publicar_artigo'),
    path('editor', editor, name='editor'),
]