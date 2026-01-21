from django.urls import path
from . import views

urlpatterns = [
    path("" , views.home , name="home"),
    path("upload_medicine/" , views.upload_medicine , name='upload_medicine'),
    path("history/" , views.History , name='history'),
     path("delete/<int:id>/", views.delete_medicine, name="delete_medicine"),
]
