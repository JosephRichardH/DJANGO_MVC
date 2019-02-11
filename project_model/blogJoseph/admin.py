from django.contrib import admin

# Register your models here.
from .models import Person, BlogPost


admin.site.register([
    Person, 
    BlogPost
])
#RumahSakit
#KebunBinatang
# admin.site.register([
#     Person, 
#     BlogPost
# ])
# #StrukturATA
# admin.site.register([
#     Person, 
#     BlogPost
# ])