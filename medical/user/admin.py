from django.contrib import admin
from .models import *

# -------------------------
# Medicine Admin
# -------------------------
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'img', 'description']

admin.site.register(Medicine, MedicineAdmin)

class MedicineDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'medicine', 'description', 'price', 'expdate', 'manufacturer']
admin.site.register(MedicineDetails , MedicineDetailsAdmin)

# -------------------------
# User Admin
# -------------------------
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'password', 'confirm_password']

admin.site.register(UserData, UserDataAdmin)


# -------------------------
# Labtest (Carousel)
# -------------------------
class LabtestAdmin(admin.ModelAdmin):
    list_display = ['id', 'img1', 'img2', 'img3']

admin.site.register(Labtest, LabtestAdmin)


# -------------------------
# Labtest Items
# -------------------------
class LabtestitemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'img', ]

admin.site.register(Labtestitems, LabtestitemsAdmin)


# -------------------------
# Labtest Item Details
# -------------------------
class LabtestitemsdetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'item', 'description', 'price']

admin.site.register(Labtestitemsdetails, LabtestitemsdetailsAdmin)


# ------------------------- doctor admin ----------------------------

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'img1', 'img2', 'img3']
admin.site.register(Doctor, DoctorAdmin)


class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'profession' , 'img' , 'degree']
admin.site.register(DoctorProfile , DoctorProfileAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'doctorname' , 'username' , 'email' , 'phone' , 'date' , 'disease' , 'prescription']
admin.site.register(Appointment , AppointmentAdmin)

class ComplaintAdmin(admin.ModelAdmin):
       list_display = ['id', 'title', 'date', 'created_at']
admin.site.register(Complaint, ComplaintAdmin)

@admin.register(SellerUser)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'username', 'email', 'owner_name', 'store_city', 'store_state', 'created_at')
    search_fields = ('store_name', 'username', 'email', 'owner_name', 'store_city')
    list_filter = ('store_city', 'store_state')

@admin.register(WholesellerUser)
class WholesellerUserAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'owner_name', 'owner_email', 'username')
    search_fields = ('company_name', 'owner_name', 'owner_email', 'username')