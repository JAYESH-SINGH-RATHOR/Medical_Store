from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from .models import *
from user.models import SellerUser , WholesellerUser
from user.views import seller_dashboard
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    wholeseller_id = request.session.get('wholeseller_id')
    if not wholeseller_id:
        return redirect('wholeseller_login')

    wholeseller = get_object_or_404(WholesellerUser, id=wholeseller_id)
    return render(request,"wholeseller/personal_details.html",{'wholeseller': wholeseller})

@login_required
def upload_medicine(request):
    if request.method == "POST":
        name = request.POST.get("medicine_name")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        Medicine.objects.create(
            wholesaler=request.user,
            name=name,
            price=price,
            image=image
        )

    return render(request , "wholeseller/upload_medicine.html")

@login_required
def History(request):
   medicines = Medicine.objects.filter(wholesaler=request.user)
   return render(request, "wholeseller/history.html", {'medicines': medicines})

@login_required
def delete_medicine(request, id):
    medicine = get_object_or_404(
        Medicine,
        id=id,
        wholesaler=request.user
    )
    medicine.delete()
    return redirect('history')


def registration(request):
    return render(request , "wholeseller/registration.html")

def login(request):
    return render(request , "wholeseller/login.html")

