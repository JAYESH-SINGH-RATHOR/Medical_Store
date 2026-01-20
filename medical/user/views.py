from django.http import HttpResponse 
from django.shortcuts import render , redirect
from httpcore import request
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404

def home(request):
    return render(request , 'user/index.html')

def test(request):
    labtests = Labtest.objects.all()
    items = Labtestitems.objects.all()

    return render(request, "user/LabTest.html", {
        "labtests": labtests,
        "items": items
    })



def labtest_detail(request, labtest_id):
    labtest = get_object_or_404(Labtest, id=labtest_id)
    items = labtest.items.all()

    return render(request, "user/labtest_detail.html", {
        "labtest": labtest,
        "LabtestDatass": items
    })



def lab_item_details(request, labtest_id, item_id):
    # Labtestitemdetailss = Labtestitemsdetails.objects.get(id=item_id)
    Labtestitemdetailss = get_object_or_404(Labtestitemsdetails, id=item_id)

    return render(request, "user/lab_item_details.html", {
        "Labtestitemdetailss": Labtestitemdetailss
    })


def doctor(request):
    doctors = Doctor.objects.all()
    doctorProfile = DoctorProfile.objects.all()
    return render(request , "user/Doctor.html", {"doctors": doctors, "doctorProfile": doctorProfile})

def doctor_profile(request, doctor_id):
    doctor = get_object_or_404(DoctorProfile, id=doctor_id)
    if request.method == "POST":
        doctorname = request.POST.get('doctorname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        disease = request.POST.get('disease')
        prescription = request.FILES.get('prescription')
        appointment = Appointment(
            doctorname=doctorname,
            username=username,
            email=email,
            phone=phone,
            date=date,
            disease=disease,
            prescription=prescription
        )
        appointment.save()
    return render(request, "user/doctor_profile.html", {"doctor": doctor})

def registration(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       email = request.POST.get("email")
       password = request.POST.get('password')
       confirm_password = request.POST.get("confirm_password")
       user = UserData(username = username , email = email , password = password , confirm_password = confirm_password)
       user.save()
    return render(request, "user/registration.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, "user/login.html")


@login_required(login_url='login')
def dashboard(request):
    return render(request, "user/dashboard.html")

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, "user/medicine.html", {"medicines": medicines})

def medicine_detail(request, id):
    medicine = Medicine.objects.get(id=id)
    details = MedicineDetails.objects.filter(medicine=medicine)
    return render(request, "user/medicinedetails.html",{"medicine": medicine, "details": details})

# Add to cart
def add_to_cart(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    else:
        cart[str(id)] = {
            'name': medicine.title,
            'price': float(medicine.details.first().price),
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('cart')


# Cart page
def cart_view(request):
    cart = request.session.get('cart', {})
    total = 0

    for item in cart.values():
        item['item_total'] = item['price'] * item['quantity']  # ✅ per item total
        total += item['item_total']

    request.session['cart'] = cart
    return render(request, 'user/AddCart.html', {
        'cart': cart,
        'total': total
    })

# Increase quantity
def increase_quantity(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    request.session['cart'] = cart
    return redirect('cart')


# Decrease quantity
def decrease_quantity(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)]['quantity'] -= 1
        if cart[str(id)]['quantity'] <= 0:
            del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart')

# Place order
def place_order(request):
    cart = request.session.get('cart')

    if not cart:
        return redirect('cart')

    total = sum(item['price'] * item['quantity'] for item in cart.values())
    request.session['order_total'] = total

    return redirect('address_page')


def address_page(request):
    if request.method == "POST":
        request.session['address'] = {
            "name": request.POST['name'],
            "phone": request.POST['phone'],
            "location": request.POST['location'],
            "building": request.POST['building'],
            "address": request.POST['address'],
            "pincode": request.POST['pincode'],
        }
        return redirect('payment_page')

    return render(request, 'user/address.html')

def payment_page(request):
    total = request.session.get('order_total')
    return render(request, 'user/payment.html', {'total': total})

def order_success(request):
    total = request.session.get('order_total')
    request.session.pop('cart', None)

    return render(request, 'user/success.html', {'total': total})