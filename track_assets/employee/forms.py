from .models import *
from django import forms

class Employee_form(forms.ModelForm):
    
    class Meta: 
        model = Employee
        fields = ('__all__')
        exclude = ('is_return',)

class payment_form(forms.ModelForm):
    class Meta:
        model = payment_way
        fields = ['payment_method']