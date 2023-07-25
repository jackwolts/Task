from django.contrib import auth

from . models import Form
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def form(request):
    if request.method=='POST':
            username=request.POST.get('name')
            email=request.POST.get('email')
            user=auth.authenticate(username=username,email=email)

            if user is not None:
                auth.login(request.request, user)
            return redirect('home')



    return render(request, 'form.html')

def home(request):
    return render(request, 'home.html')




