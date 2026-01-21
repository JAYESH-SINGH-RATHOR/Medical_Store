from django.contrib import admin
from .models import *
# Register your models here.
class bulkMedicineAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name', 'price', 'medicine_file')
admin.site.register(bulkMedicine, bulkMedicineAdmin)

class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id' ,'wholesaler', 'name', 'price', 'medicine_file', 'uploaded_at')
admin.site.register(Medicine, MedicineAdmin)