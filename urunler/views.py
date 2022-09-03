from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    urunler = Urun.objects.all()
    kategoriler = Kategori.objects.all()
    
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        urunler = Urun.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    context = {
        'urunlerim':urunler,
        'search':search,
        'kategori':kategoriler,
    }
    return render(request, 'index.html', context)

def urun(request, urunId):
    urun = Urun.objects.filter(id = urunId)
    kategoriler = Kategori.objects.all()
    print(urun)
    context = {
        'urun':urun,
        'kategori':kategoriler
    }
    return render(request, 'urun.html', context)

def olustur(request):
    kategoriler = Kategori.objects.all()
    if request.method == 'POST':
        resim = request.FILES['resim']
        isim = request.POST['isim']
        aciklama = request.POST['aciklama']
        fiyat = request.POST['fiyat']

        urun = Urun.objects.create(
            isim = isim, 
            aciklama = aciklama, 
            fiyat = fiyat, 
            resim = resim
        )

        urun.save()
        
        print("Ürün oluşturuldu")
        return redirect('index')
    context = {
        'kategoriler':kategoriler
    }
    return render(request, 'olustur.html')

