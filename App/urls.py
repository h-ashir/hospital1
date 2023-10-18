from django.urls import path,include
from App import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('doctors/',views.doctors,name="doctors"),
    path('booking/',views.booking,name="booking"),
    path('department/',views.department,name="department"),
    path('contact/',views.contact,name="contact"),
    path('confirmation/',views.confirmation,name="confirmation"),
]