from django.urls import path
from . import views
from user.views import *
urlpatterns = [
    path("" , views.home , name="wholeseller_home"),
    path("upload_medicine/" , views.upload_medicine , name='upload_medicine'),
    path("history/" , views.History , name='history'),
     path("delete/<int:id>/", views.delete_medicine, name="delete_medicine"),
     path('wholeseller_dashboard/', seller_dashboard, name='seller_dashboard'),
    # path("registration/" , views.registration , name='registration'),
    # path("login/" , views.login , name='login'),
]
