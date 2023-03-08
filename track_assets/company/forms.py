from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Import Models
from .models import *
       

class DevicesForm(forms.ModelForm):
    
    class Meta:
        model = Device
        fields = ('__all__')
        exclude = ('user','slug')
        widgets = {
            'name': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Device Name'}),
            'price': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        }