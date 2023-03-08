from django.shortcuts import render, redirect
from employee.forms import *
from django.views.generic import TemplateView
from employee.models import *
from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import *
# Create your views here.




# this class is for employe table 
class EmployeesView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            employees = Employee.objects.filter(user = request.user)

            context = {
                'employees': employees
            }
            return render(request, 'company/index.html', context)
        else:
            return redirect('home')
    def post(self, request, *args, **kwargs):
        pass


# views for employee registration
def add_employee(request):
    
    forms = Employee_form()
    # user_data = User.objects.get(user = request.user)
    # user_data = User.objects.get(request.user.username)
    if request.method == 'POST':
        device = Device.objects.filter(user = request.user)
        forms = Employee_form(request.POST)
        if forms.is_valid():
            form_data = forms.save(commit=False)
            form_data.user = request.user
            forms.save()
            forms.save_m2m()

            return redirect('home')
    else:
        forms = Employee_form()
    context = {
        'forms' : forms
    }
    return render(request, 'company/add-employee.html',context)        
        

# payment gateway method 
def payment_getway(request):
    forms =  payment_form()

    context= {
        'forms': forms
    }

    return render(request, 'company/payment.html', context)


def add_devices(request):
    device_form = DevicesForm()
    if request.method == 'POST':       
        device_form = DevicesForm(request.POST, request.FILES)
        if device_form.is_valid():
            device_form = device_form.save(commit=False)
            device_form.user = request.user
            device_form.save()
            messages.success(request, 'Save Successfully !!')
            return HttpResponseRedirect(request.path_info)
    
    context = {
        'device_form': device_form
    }
    return render(request, 'device/add_device.html', context)
