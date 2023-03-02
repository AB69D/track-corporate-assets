from django.shortcuts import render, redirect
from employee.forms import Employee_form
from django.views.generic import TemplateView
from employee.models import *
# Create your views here.

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

def add_employee(request):
    
    forms = Employee_form()
    # user_data = User.objects.get(user = request.user)
    # user_data = User.objects.get(request.user.username)
    if request.method == 'POST':
        if request.user.is_authenticated:
            forms = Employee_form(request.POST,  request.FILES, instance=request.user)

            if forms.is_valid():
                forms.save()

                return redirect('home')
    else:
        forms = Employee_form()
    context = {
        'forms' : forms
    }
    return render(request, 'company/add-employee.html',context)        
        