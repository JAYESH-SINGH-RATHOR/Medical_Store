from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render(request , "wholeseller/personal_details.html")

def upload_medicine(request):
    if request.method == "POST":
        name = request.POST.get("medicine_name")
        price = request.POST.get("price")
        medicine_file = request.FILES.get("medicine_file")
        item = bulkMedicine(name=name, price=price, medicine_file=medicine_file)
        item.save()
    return render(request , "wholeseller/upload_medicine.html")

def History(request):
    medicines = bulkMedicine.objects.all()
    return render(request, "wholeseller/history.html", {'medicines': medicines})

def delete_medicine(request, id):
    medicine = get_object_or_404(bulkMedicine, id=id)
    medicine.delete()
    return redirect('history')


