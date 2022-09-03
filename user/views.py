from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from urunler.models import *
from urunler.models import *
# Create your views here.
def userRegister(request):
    kategoriler = Kategori.objects.all()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print("Kullanıcı oluşturuldu..")
            return redirect('login')
    context = {
        'form':form,
        'kategori': kategoriler
    }
    return render(request, 'register.html', context)

def userLogin(request):
    kategoriler = Kategori.objects.all()
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print("Kullanıcı adı veya şifre hatalı")
            return redirect('login')
    context = {
        'kategori':kategoriler
    }
    return render(request, 'login.html', context)

def userLogout(request):
    logout(request)
    return redirect('index')