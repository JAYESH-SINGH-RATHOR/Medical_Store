from django.shortcuts import render , redirect, get_object_or_404
from user.models import *
from user.views import *
from .models import *

# Create your views here.

def home(request):
    seller_id = request.session.get('seller_id')
    if not seller_id:
        return redirect('seller_login')
    seller = get_object_or_404(SellerUser, id=seller_id)
    return render(request , "seller/seller_dashboard.html" , {'seller' : seller})