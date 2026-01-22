from django.urls import path
from .import views
urlpatterns = [
    path("" , views.home , name="seller_home"),
    path("add_medicine/" , views.add_medicine , name="add_medicine"),
    path("add_medicine/<int:medicine_id>/" , views.add_medicine_details , name="add_medicine_details"),
    path("contact/" , views.contact , name="contact"),
    # path("cart/" , views.cart , name="cart"),
    path('medicine/', views.medicine_page, name='medicine')
]
