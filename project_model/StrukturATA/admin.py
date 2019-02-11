from django.contrib import admin
from .models import Direksi,Mentee,Mata_Pelajaran,Mentor,Challenge,Live_Code

# Register your models here.
#RumahSakit
admin.site.register([
    Direksi,
    Mentee,
    Mata_Pelajaran,
    Mentor,
    Challenge,
    Live_Code
])