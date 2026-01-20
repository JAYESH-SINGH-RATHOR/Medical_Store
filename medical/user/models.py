from django.db import models

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
        related_name="details"
    )
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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