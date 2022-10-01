from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lancamento
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.views import serve

@login_required(redirect_field_name='login')
def index(request):
    lancamentos = Lancamento.objects.order_by('data')
    paginator = Paginator(lancamentos, 10)
    page = request.GET.get('p')
    lancamentos = paginator.get_page(page)
    
    return render(request, 'razao/index.html', {
        'lancamentos': lancamentos
    })

def ver_lancamento(request, lancamento_id):
    #contato = Contato.objects.get(id=contato_id)
    lancamento = get_object_or_404(Lancamento, id=lancamento_id)

    return render(request, 'razao/ver_lancamento.html', {
        'lancamento': lancamento
    })

def busca(request):
    termo = request.GET.get('termo')   

    if termo is None or not termo:
        messages.add_message(
            request, 
            messages.ERROR, 
            'Campo de busca vazio'
        )
        return redirect(to='index')

    lancamentos = Lancamento.objects.filter(
        Q(nome__icontains=termo) | Q(valor__icontains=termo)
    )

    if not lancamentos:
        messages.add_message(
            request,
            messages.ERROR,
            'Nenhum resultado para busca'
        )
        return redirect(to='index')

    paginator = Paginator(lancamentos, 5)
    page = request.GET.get('p')
    lancamentos = paginator.get_page(page)
    
    return render(request, 'razao/busca.html', {
        'lancamentos': lancamentos
    })

def ver_arquivo(request, serve):
    return render(serve, request, 'arquivos')