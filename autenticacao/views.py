from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django. contrib.auth.decorators import login_required
from django.contrib import messages
from autenticacao.forms import LoginForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.error(request, 'E-mail ou senha inválidos.')
    else:
        form = LoginForm()
    return render(request, 'autenticacao/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')