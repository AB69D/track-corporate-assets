from .models import *
from django import forms

class Employee_form(forms.ModelForm):
    
    class Meta: 
        model = Employee
        fields = ('__all__')
        exclude = ('user', 'is_return')