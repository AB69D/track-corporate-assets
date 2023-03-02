from django.shortcuts import render
from .forms import Employee_form
from .models import *
# Create your views here.

# def employees(request):
#     if request.user.is_authenticated:
#         employee = Employee.objects.all()

#     context = {
#         'employees' : employee
#     }
    
#     return render(request, 'company/index.html',context)


