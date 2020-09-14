from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'index.html')


def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect(reverse('home'))
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect(reverse('home'))
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def log_out(request):
    logout(request)
    return redirect(reverse('home'))