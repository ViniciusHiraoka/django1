from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto

def index(request):
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado!'
    else:
        teste = 'Usuário logado!'

    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação web com Django',
        'outro': 'sucumba saydeira!!!',
        'logado': teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render())

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render())