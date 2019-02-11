from django.db import models
from django.db.models import TextField
from django.utils import timezone
# Create your models here.
#modelRumahsakit

#modelKebunBinatang

class Hewan(models.Model):
    name = models.CharField(max_length=255)
    species = models.TextField(max_length=25)
    berat = models.PositiveIntegerField()
    umur = models.PositiveIntegerField()

class Kandang(models.Model):
    name = models.CharField(max_length=255)
    isi_kandang = models.PositiveIntegerField()
    luas_kandang = models.FloatField()

class Penjaga(models.Model):
    name = models.CharField(max_length=255)
    nomor_telepon = models.PositiveIntegerField()
    jadwal_jaga = models.DateTimeField(default=timezone.now)

class Pengunjung(models.Model):
    name = models.CharField(max_length=255)
    nomor_telepon = models.TextField(max_length=25)
    hari_berkunjung = models.DateTimeField(default=timezone.now)

