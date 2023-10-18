from django import forms
from .models import Booking
    
class DateInput(forms.DateInput):
        input_type = "date" 
    
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
    
        labels = {
            'p_name' : 'Patient Name',
            'p_phone' : 'Phone number',
            'p_email' : 'Email Address',
            'doc_name' : 'Doctor'
        }
        widgets = {
            'booking_date' : DateInput(),
            # 'p_name': forms.TextInput(attrs={'class': 'patient-name-class', 'id': 'custom-input-id'}),
            # 'p_phone': forms.TextInput(attrs={'class': 'phone-input-class'}),
        }
