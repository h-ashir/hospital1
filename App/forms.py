from django import forms
from .models import Booking
    
class DateInput(forms.DateInput):
        input_type = "date" 
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        # fields = [
        #      'p_name',
        #      'p_phone',
        #      'p_email',
        #      'doc_name',
        #      'booking_date',
        # ]
    
        labels = {  
            'p_name' : 'Patient Name',
            'p_phone' : 'Phone number',
            'p_email' : 'Email Address',
            'doc_name' : 'Doctor'
        }
        widgets = {
            'booking_date' : DateInput(),
            'p_name': forms.TextInput(attrs={'class': 'patient-input-class'}),
            'p_phone': forms.TextInput(attrs={'class': 'phone-input-class'}),
            'p_email': forms.TextInput(attrs={'class': 'email-input-class'}),
            'doc_name': forms.Select(attrs={'class': 'doc-input-class'}),
        }
