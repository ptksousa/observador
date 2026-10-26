from django.shortcuts import render, redirect
from django.http import HttpResponse

from usuarios.forms import CadastroForms

from django.contrib.auth.models import User

def index(request):
    return HttpResponse('<h1>Olá mundo</h1>')

def login(request):
    return HttpResponse('<h1>login</h1>')

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
                
                if form["senha_1"].value() != form["senha_2"].value():
                    return redirect('cadastro')
                
                nome=form["usuario"].value()
                email=form["email"].value()
                senha=form["senha_1"].value()

                if User.objects.filter(username=nome).exists():
                    return redirect('cadastro')

                usuario = User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha
                )
                usuario.save()
                return redirect('login')

    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    return HttpResponse('<h1>logout</h1>')
