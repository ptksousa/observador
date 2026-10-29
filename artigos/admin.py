from django.contrib import admin
from .models import Artigo

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao', 'publicado')
    search_fields = ('titulo',)
    list_filter = ('autor', 'data_criacao')
    list_editable = ("publicado",)
    list_per_page = 10

    