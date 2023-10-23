from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Department,Doctors
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def doctors(request):
    dict_doc = {
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)

def department(request):
    dict_dept = {
        'dept': Department.objects.all()
    }
    return render(request,'department.html',dict_dept)

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmation')
    else:
        form = BookingForm()
    form = BookingForm()
    dict_booking = {
        'form' : form
    }   
    return render(request,'booking.html',dict_booking)

def contact(request):
    return render(request,'contact.html')

def confirmation(request):
    return render(request,'confirmation.html')