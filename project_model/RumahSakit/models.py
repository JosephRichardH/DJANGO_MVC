from django.db import models
from django.db.models import TextField
from django.utils import timezone
# Create your models here.
#modelRumahsakit

class Dokter(models.Model):
    name = models.CharField(max_length=255)
    telephone = models.TextField(max_length=25)
    bidang = models.CharField(max_length=255)
    jadwal_praktek = models.DateTimeField(default=timezone.now)

class Pasien(models.Model):
    name = models.CharField(max_length=255)
    telephone = models.PositiveIntegerField()
    alamat = models.CharField(max_length=255)
    keluhan = models.CharField(max_length=255)

class Resep(models.Model):
    name = models.CharField(max_length=255)
    total_harga = models.PositiveIntegerField()
    kumpulan_obat = models.CharField(max_length=255)

class Obat(models.Model):
    name = models.CharField(max_length=255)
    kandungan = models.CharField(max_length=255)    
    khasiat = models.CharField(max_length=255)