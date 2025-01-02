from django.shortcuts import render,redirect # type: ignore
from home.forms import RegisterForm # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib import auth # type: ignore
from django.contrib.auth import login as auth_login

def register(request):

    form = RegisterForm()   

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Usuário logado')
            return redirect('home:login')

    context = {
        'form': form,
        'title': 'Register',
    }

    return render(request,'home/user/register.html',context)

def login_view(request):
    form = AuthenticationForm(request, data=request.POST if request.method == 'POST' else None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('home:index')

        messages.error(request, 'Erro ao realizar login')

    context = {
        'form': form,
        'title': 'login',
    }
    return render(request, 'home/user/login.html', context)

def logout_view(request):

    auth.logout(request)

    return redirect('home:login')

def user_update(request):

    form = RegisterForm(instance=request.user)

    context = {
        'form': form,
        'title': 'Update User'
    }


    if request.method!='POST':
        return render(request,'home/user/update.html',context)

    form = RegisterForm(data=request.POST, isinstance=request.user)

    if not form.is_valid():
        return render(request,'home/user/update.html',context)
    
    form.save()

    return redirect('home:user_update')


