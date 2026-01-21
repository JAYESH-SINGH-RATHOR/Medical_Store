from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class bulkMedicine(models.Model):
    wholesaler = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='medicine_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class Medicine(models.Model):
    wholesaler = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
