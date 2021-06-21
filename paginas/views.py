from django.shortcuts import render
from .models import *

def home(request):
    url = request.get_full_path()
    projetos = Projeto.objects.all()
    tecnologias = Tecnologias.objects.all()
    context = {'projetos':projetos, 'tecnologias':tecnologias}
    return render(request,'paginas/home.html', context)

def projeto(request, slug):
    projetos = Projeto.objects.get(slug=slug)
    context = {'projetos':projetos}
    return render(request,'paginas/projeto.html', context)