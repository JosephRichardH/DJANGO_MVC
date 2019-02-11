from django.contrib import admin
from .models import Hewan,Kandang,Penjaga,Pengunjung

# Register your models here.
#RumahSakit
admin.site.register([
    Hewan,
    Kandang,
    Penjaga,
    Pengunjung
])