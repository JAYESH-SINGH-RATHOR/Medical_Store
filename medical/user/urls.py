from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('test/<int:labtest_id>/', views.labtest_detail, name='labtest_detail'),
    path('test/<int:labtest_id>/item/<int:item_id>/',views.lab_item_details ,name='lab_item_details'),
    path('doctor', views.doctor, name='doctor'),
    path('doctor/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),
    path('registration', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
    path('medicine/', views.medicine_list, name='medicine_list'),
    path('medicine/<int:id>/', views.medicine_detail, name='medicine_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
     path('place-order/', views.place_order, name='place_order'),
    path('address/', views.address_page, name='address_page'),
    path('payment/', views.payment_page, name='payment_page'),
    path('success/', views.order_success, name='order_success')


]
