from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Olá mundo</h1>')

def editor(request):
    return render(request, 'artigos/editor.html')