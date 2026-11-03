from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from artigos.models import Artigo

def index(request):
    lista_artigos = Artigo.objects.all().order_by('-data_criacao').filter(publicado=True)
    contexto = {
        'artigos': lista_artigos
    }
    return render(request, 'artigos/index.html', contexto)

def editor(request):
    if request.method == 'POST':
        titulo_digitado = request.POST.get('titulo')
        conteudo_do_quill = request.POST.get('conteudo')
        capa_enviada = request.FILES.get('imagem_capa')
        
        autor_logado = request.user 

        novo_artigo = Artigo.objects.create(
            titulo=titulo_digitado,
            imagem_capa=capa_enviada,
            conteudo=conteudo_do_quill,
            autor=autor_logado
        )
        novo_artigo.save()

        return redirect('index') 

    return render(request, 'artigos/editor.html')