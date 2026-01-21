from django.db import models

# Create your models here.

class bulkMedicine(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    medicine_file = models.FileField(upload_to='')

    def __str__(self):
        return self.name

class Medicine(models.Model):
    wholesaler = models.ForeignKey("auth.User" , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    medicine_file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

