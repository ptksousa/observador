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
        # 1. Pega os dados do HTML (o name="titulo" e o name="conteudo")
        titulo_digitado = request.POST.get('titulo')
        conteudo_do_quill = request.POST.get('conteudo')
        
        # 2. Pega o usuário que está logado no momento
        autor_logado = request.user 

        # 3. Salva no banco de dados!
        novo_artigo = Artigo.objects.create(
            titulo=titulo_digitado,
            conteudo=conteudo_do_quill,
            autor=autor_logado
            # data_criacao é automático, não precisamos passar
        )
        novo_artigo.save()

        # Depois de salvar, manda o usuário de volta pra página inicial
        return redirect('index') 

    # Se não for POST (se a pessoa só abriu a página), exibe a tela do editor
    return render(request, 'artigos/editor.html')