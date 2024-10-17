from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomPasswordChangeForm  # Use o CustomUserCreationForm em vez de RegisterForm
from .models import Item  # Certifique-se de ter um modelo Item criado
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # Use CustomUserCreationForm
        if form.is_valid():
            user = form.save()  # Salva o usuário
            messages.success(request, 'Cadastro realizado com sucesso!')  # Exibe a mensagem de sucesso
            return redirect('login')  # Redireciona para a página de login
    else:
        form = CustomUserCreationForm()  # Exibe o formulário em branco para GET
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Senha alterada com sucesso!')  # Adicione uma mensagem de sucesso
            return redirect('login')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


# View para lista de itens paginada
def item_list_view(request):
    items = Item.objects.all()  # Certifique-se de que Item esteja corretamente modelado
    return render(request, 'items.html', {'items': items})
