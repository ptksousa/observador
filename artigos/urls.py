from artigos.views import index, editor, redacao, publicar_artigo, editar_artigo, excluir_artigo
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('redacao', redacao, name='redacao'),
    path('redacao/publicar/<int:id>/', publicar_artigo, name='publicar_artigo'),
    path('redacao/editar/<int:id>/', editar_artigo, name='editar_artigo'),
    path('redacao/excluir/<int:id>/', excluir_artigo, name='excluir_artigo'),
    path('editor', editor, name='editor'),
]