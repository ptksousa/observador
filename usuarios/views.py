from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Olá mundo</h1>')

def login(request):
    return HttpResponse('<h1>login</h1>')

def cadastrar(request):
    return HttpResponse('<h1>cadastro</h1>')

def logout(request):
    return HttpResponse('<h1>logout</h1>')
