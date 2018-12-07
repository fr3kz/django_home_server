from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)        
    upload = models.FileField(upload_to='files/')
    usr = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return "plik"    
