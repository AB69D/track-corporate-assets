from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# registration form for user 
class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-box', 'placeholder': 'Username'}),label = False)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control input-box', 'placeholder': 'Email Address'}),label = False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-box', 'placeholder': 'Password'}),label = False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-box', 'placeholder': 'Confirm Password'}),label = False)
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data['password1']
        confirm_pass = self.cleaned_data['password2']
        if password != confirm_pass:
            raise forms.ValidationError("Password Doesn't Match")  