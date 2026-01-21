from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required

from WholeSeller.models import Medicine
from Seller.models import *
from user.models import MedicineDetails, SellerUser



def home(request):
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect('seller_login')

    seller = get_object_or_404(SellerUser, id=seller_id)
    return render(request, "seller/seller_dashboard.html", {'seller': seller})


@login_required
def add_medicine(request):
    medicines = Medicine.objects.filter(wholesaler=request.user)
    return render(request, "seller/add_medicine.html", {'medicines': medicines})


def add_medicine_details(request, medicine_id):
    details = get_object_or_404(Medicine, id=medicine_id)
    return render(request, "seller/add_medicine_details.html" , {'details': details})


def contact(request):
    return render(request, "seller/contact.html")


def cart(request):
    return render(request, "seller/cart.html")

def medicine_page(request):
    return render(request, "seller/medicine.html")
