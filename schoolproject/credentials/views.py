from django.contrib import auth, messages
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,"invailed credentials")
            return redirect('login')
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

