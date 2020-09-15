from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'index.html', locals())


def my_profile(request):
    return render(request, 'accounts/profile.html', locals())


def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def sign_in(request):
    err_msg = ''
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            err_msg = 'Login pass'
            return redirect('home')
        else:
            err_msg = 'Login fail'
    context = {
        'form': form,
        'err_msg': err_msg,
    }
    return render(request, 'accounts/login.html', context)


def log_out(request):
    logout(request)
    return redirect('home')
