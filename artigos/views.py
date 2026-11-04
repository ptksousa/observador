from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from artigos.models import Artigo

def index(request):
    lista_artigos = Artigo.objects.all().order_by('-data_criacao').filter(publicado=True)
    
    eh_autor = False
    if request.user.is_authenticated:
        eh_autor = request.user.groups.filter(name='autores').exists() or request.user.is_superuser
    
    contexto = {
        'artigos': lista_artigos,
        'eh_autor': eh_autor 
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

def redacao(request):
    if not request.user.groups.filter(name='autores').exists() and not request.user.is_superuser:
        return redirect('index')

    todos_artigos = Artigo.objects.all().order_by('-data_criacao')
    
    return render(request, 'artigos/redacao.html', {'artigos': todos_artigos})

def publicar_artigo(request, id):
    if not request.user.groups.filter(name='autores').exists() and not request.user.is_superuser:
        return redirect('index')

    artigo = get_object_or_404(Artigo, id=id)
    
    artigo.publicado = not artigo.publicado
    artigo.save()
    
    return redirect('redacao')

def editar_artigo(request, id):
    if not request.user.groups.filter(name='autores').exists() and not request.user.is_superuser:
        return redirect('index')

    artigo = get_object_or_404(Artigo, id=id)

    if request.method == 'POST':
        artigo.titulo = request.POST.get('titulo')
        artigo.conteudo = request.POST.get('conteudo')
        
        nova_capa = request.FILES.get('imagem_capa')
        if nova_capa:
            artigo.imagem_capa = nova_capa
            
        artigo.save()
        return redirect('redacao')

    return render(request, 'artigos/editor.html', {'artigo': artigo})

def excluir_artigo(request, id):
    if not request.user.groups.filter(name='autores').exists() and not request.user.is_superuser:
        return redirect('index')

    artigo = get_object_or_404(Artigo, id=id)
    artigo.delete() 
    
    return redirect('redacao')


    