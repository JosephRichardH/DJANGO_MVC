from django.db import models
from django.db.models import TextField
from django.utils import timezone
#from django.db import models as Models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.TextField(max_length=255)
    gender = models.CharField(max_length=1)
    telephone = models.TextField(max_length=25)
    mobile = models.TextField(max_length=25)
    address = models.TextField(max_length=255)

class BlogPost(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    posts = models.TextField(max_length=255)
