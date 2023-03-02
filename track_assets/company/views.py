from django.shortcuts import render, redirect
from employee.forms import Employee_form
from django.views.generic import TemplateView
from employee.models import *
# Create your views here.

class EmployeesView(TemplateView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()

        context = {
            'employees': employees
        }
        return render(request, 'company/index.html', context)
    def post(self, request, *args, **kwargs):
        pass

def add_employee(request):
    
    forms = Employee_form()

    if request.method == 'POST':

        forms = Employee_form(request.POST,  request.FILES)

        if forms.is_valid():
            forms.save()

            return redirect('home')
    else:
        forms = Employee_form()
    context = {
        'forms' : forms
    }
    return render(request, 'company/add-employee.html',context)        
        