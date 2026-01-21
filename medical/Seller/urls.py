from django.urls import path
from .import views
urlpatterns = [
    path("" , views.home , name="seller_home"),
    path("add_medicine/" , views.add_medicine , name="add_medicine"),
    path("contact/" , views.contact , name="contact"),
    path("cart/" , views.cart , name="cart"),
    path("medicine/" , views.medicine , name="medicine"),
]
