from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormLancamento

# Create your views here.

def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')

    else:
        auth.login(request, user)
        messages.success(request, 'Você está logado.')
        return redirect('index')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Você está desconectado.')
    return redirect('index')

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    lista_codigos_empresas = {
        '1178': 'Picoleve',
    }

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    codigo = request.POST.get('codigo')

    if not nome or not email or not usuario or not senha or not senha2:
        print(nome, email, usuario, senha, senha2)
        messages.error(request, 'Nenhum campo pode ficar vazio.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
       
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/register.html')

    if codigo not in lista_codigos_empresas:
        messages.error(request, 'Código não pertence a nenhuma empresa cadastrada.')
        return render(request, 'accounts/register.html')

    if len(senha) <= 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais')
        return render(request, 'accounts/register.html')

    if len(usuario) <= 6:
        messages.error(request, 'Usuario precisa ter 6 caracteres ou mais')
        return render(request, 'accounts/register.html')

    if senha != senha2:
        messages.error(request, 'As senhas precisam ser iguais.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário escolhido já existe.')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado.')

    user = User.objects.create_user(username=usuario, email=email, 
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    messages.success(request, 'Registrado com sucesso. Agora faça seu login.')
    return redirect('login')

@login_required(redirect_field_name='login')
def novo_lancamento(request):
    if request.method != 'POST':
        form = FormLancamento()
        return render(request, 'accounts/novo_lancamento.html', {'form':form})

    form = FormLancamento(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormLancamento(request.POST)
        return render(request, 'accounts/novo_lancamento.html', {'form': form})

    form.save()
    messages.success(request, 'Lançamento feito com sucesso.')
    return redirect('novo_lancamento')
