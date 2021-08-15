from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserForm

# Create your views here.
def register(request):
    page_title = "Register Page"
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/dashboard')
        else:
            return render(request, 'authentication/register.html', {
                'page_title': page_title,
                'error': "Please, fill out all fields.",
                'form': form
            })
    else:
        return render(request, 'authentication/register.html', {
            'page_title': page_title,
            'form': form
        })

def login(request):
    page_title = "Login Page"
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('/dashboard')
    
    return render(request, 'authentication/login.html', {
        'page_title': page_title,
        'form': form,
    })

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('/')
    else:
        return redirect('/authentication/login')