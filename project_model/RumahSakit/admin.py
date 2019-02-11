from django.contrib import admin
from .models import Dokter, Pasien, Resep, Obat

# Register your models here.
#RumahSakit
admin.site.register([
    Dokter, 
    Pasien,
    Resep,
    Obat
])