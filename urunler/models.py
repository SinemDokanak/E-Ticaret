
from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=50)
    def __str__(self):
        return self.isim
class AltKategori(models.Model):
    isim = models.CharField(max_length=50)

    def __str(self):
        return self.isim

class Ornek(models.Model):
    isim = models.CharField(max_length=50)
    def __str__(self):
        return self.isim
class Urun (models.Model):
    kategori = models.ForeignKey(Kategori, on_delete= models.CASCADE, null= True)
    AltKategori = models.ManyToManyField(AltKategori, blank= True)
    ornek = models.OneToOneField(Ornek, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=200, verbose_name='Ürün İsmi')
    aciklama = models.TextField(max_length=400)
    fiyat = models.IntegerField()
    resim = models.FileField(upload_to='urunler/', null=True, blank=True, verbose_name='Ürün Resmi')

    def __str__(self):
        return self.isim
        