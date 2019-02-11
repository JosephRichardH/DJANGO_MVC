from django.db import models
from django.db.models import TextField
from django.utils import timezone
# Create your models here.

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.PositiveIntegerField()
    jabatan = models.CharField(max_length=255)

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.PositiveIntegerField()
    nomor_absen = models.PositiveIntegerField()
    nilai_rata2 = models.TextField(max_length=25)

class Mata_Pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=255)
    jadwal_dimulai = models.DateTimeField(default=timezone.now)
    jadwal_berakhir = models.DateTimeField(default=timezone.now)

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    nomor_telepon = models.PositiveIntegerField()
    matapelajaran = models.ForeignKey(Mata_Pelajaran,on_delete=models.CASCADE)

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.PositiveIntegerField()
    bobot_nilai = models.FloatField()
    matapelajaran = models.ForeignKey(Mata_Pelajaran,on_delete=models.CASCADE)

class Live_Code(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.PositiveIntegerField()
    bobot_nilai = models.FloatField()
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    matapelajaran = models.ForeignKey(Mata_Pelajaran,on_delete=models.CASCADE)
