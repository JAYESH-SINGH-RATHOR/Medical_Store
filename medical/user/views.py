from django.http import HttpResponse 
from django.shortcuts import render , redirect
from httpcore import request
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    crosusel = Crosusel.objects.all()
    about = About.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contactt = ContactUser(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contactt.save()

        messages.success(request, "Your query has been sent successfully!")
        return redirect("home")
    return render(request , 'user/index.html', {"crosusel": crosusel, "about": about})

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

def Orders(request):
    return render(request , 'user/login/Orders.html')

def edit_profile(request):
    return redirect("registration")

def complaint(request):
    if request.method == 'POST':
        Complaint.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            date=request.POST.get('date')
        )
        return redirect('profile')
    return render(request , 'user/login/complaint.html')

def help(request):
    return render(request , 'user/login/bot.html')

def profile(request):
    return render(request, "user/login/profile.html")


def page_not_found(request , exception):
    return render(request , "user/error.html" , status=404)

def seller_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['owner_email']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('seller_register')

        seller = SellerUser(
            username=username,
            password=password,
            email=email,
            store_name=request.POST['store_name'],
            gst_number=request.POST['gst_number'],
            store_address=request.POST['store_address'],
            store_license=request.POST['store_license'],
            store_timing=request.POST['store_timing'],
            store_city=request.POST['store_city'],
            store_state=request.POST['store_state'],
            store_pincode=request.POST['store_pincode'],
            owner_name=request.POST['owner_name'],
            owner_phone=request.POST['owner_phone'],
            store_logo=request.FILES.get('store_logo')
        )
        seller.save()
        messages.success(request, "Seller registered successfully!")
        return redirect('seller_login')
    return render(request , 'seller/seller_registration.html')

def wholeseller_registration(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            owner_email = request.POST.get('owner_email')  # <-- Match the form field
            owner_name = request.POST.get('owner_name')
            owner_phone = request.POST.get('owner_phone')
            company_name = request.POST.get('company_name')
            gst_number = request.POST.get('gst_number')
            company_address = request.POST.get('company_address')
            company_logo = request.FILES.get('company_logo')

            # Password validation
            if password != confirm_password:
                messages.error(request, "Passwords do not match!")
                return render(request, 'wholeseller_registration.html')

            # Save wholeseller
            wholeseller = WholesellerUser(
                username=username,
                password=make_password(password),  # hash password
                owner_email=owner_email,
                owner_name=owner_name,
                owner_phone=owner_phone,
                company_name=company_name,
                gst_number=gst_number,
                company_address=company_address,
                company_logo=company_logo
            )
            wholeseller.save()
            messages.success(request, "Wholeseller registered successfully!")
            return redirect('wholeseller_login')
    return render(request , 'wholeseller/wholeseller_registration.html')

def seller_login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            seller = SellerUser.objects.get(username=username)
            if check_password(password, seller.password):
                request.session['seller_id'] = seller.id
                return redirect('seller_home')  
            else:
                messages.error(request, "Incorrect password!")
        except SellerUser.DoesNotExist:
            messages.error(request, "Seller not found!")
     return render(request , 'seller/seller_login.html')

def wholeseller_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            wholeseller = WholesellerUser.objects.get(username=username)
            if check_password(password, wholeseller.password):
                request.session['wholeseller_id'] = wholeseller.id
                return redirect('wholeseller_home')
            else:
                messages.error(request, "Incorrect password!")
        except WholesellerUser.DoesNotExist:
            messages.error(request, "Wholeseller not found!")
    return render(request , 'wholeseller/wholeseller_login.html')



def seller_dashboard(request):
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect('seller_login')
    seller = get_object_or_404(SellerUser, id=seller_id)
    return render(request, 'seller/seller_dashboard.html', {'seller': seller})

def wholeseller_dashboard(request):
    wholeseller_id = request.session.get('wholeseller_id')
    if not wholeseller_id:
        return redirect('wholeseller_login')
    wholeseller = get_object_or_404(WholesellerUser, id=wholeseller_id)
    return render(request, 'wholeseller/wholeseller_dashboard.html', {'wholeseller': wholeseller})