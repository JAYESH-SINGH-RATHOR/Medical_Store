from django.db import models
from django.contrib.auth.hashers import make_password


# # -------------------------
# # Medicine
# # -------------------------
class Medicine(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='medicine_images/')
    description = models.TextField()

    def __str__(self):
        return self.title

class MedicineDetails(models.Model):
     medicine = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE,
        related_name='details'
    )
     description = models.TextField(max_length=500)
     price = models.IntegerField()
     expdate = models.DateField()
     manufacturer = models.CharField(max_length=100)

     def __str__(self):
        return f"Details of {self.medicine.title}"


# # -------------------------
# # User Data
# # -------------------------
class UserData(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Labtest(models.Model):
    img1 = models.ImageField(upload_to='labs/')
    img2 = models.ImageField(upload_to='labs/')
    img3 = models.ImageField(upload_to='labs/')

    def __str__(self):
        return f"Labtest {self.id}"


class Labtestitems(models.Model):
    labtest = models.ForeignKey(
        Labtest,
        on_delete=models.CASCADE,
        related_name="items" , null=True, blank=True
    )
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='labitems/')

    def __str__(self):
        return self.name


class Labtestitemsdetails(models.Model):
    item = models.ForeignKey(
        Labtestitems,
        on_delete=models.CASCADE,
        related_name="details"
    )
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Details of {self.item.name}"


# --------------  doctor models -------------------

class Doctor(models.Model):
    img1 = models.ImageField(upload_to='doctor/')
    img2 = models.ImageField(upload_to='doctor/')
    img3 = models.ImageField(upload_to='doctor/')

    def __str__(self):
        return f"Doctor {self.id}"
    
class DoctorProfile(models.Model):
    img = models.ImageField(upload_to='doctor_profile/')
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
    
class Appointment(models.Model):
    doctorname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    disease = models.TextField()
    prescription = models.FileField(upload_to='prescriptions/')

    def __str__(self):
        return f"Appointment with Dr. {self.doctorname} for {self.username} on {self.date}"
    

class Complaint(models.Model):
    # user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='complaints/', blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    


# =========================
# Seller Model
# =========================
class SellerUser(models.Model):
    # Login credentials
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # hashed
    email = models.EmailField(unique=True)

    # Store Information
    store_name = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=15)
    store_address = models.TextField()
    store_logo = models.ImageField(upload_to='seller_logos/', blank=True, null=True)
    store_license = models.CharField(max_length=50)
    store_timing = models.CharField(max_length=50)
    store_city = models.CharField(max_length=50)
    store_state = models.CharField(max_length=50)
    store_pincode = models.CharField(max_length=10)

    # Owner/Contact Details
    owner_name = models.CharField(max_length=100)
    owner_phone = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Hash password if not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.store_name} ({self.username})"


# =========================
# Wholeseller Model
# =========================
class WholesellerUser(models.Model):
    company_name = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=50)
    company_address = models.TextField()
    company_logo = models.ImageField(upload_to='wholeseller_logos/', blank=True, null=True)

    # Owner Details
    owner_name = models.CharField(max_length=255)
    owner_email = models.EmailField(unique=True , null=False)
    owner_phone = models.CharField(max_length=15)

    # Login Credentials
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords in production

    def __str__(self):
     return f"{self.company_name} - {self.owner_name}"
