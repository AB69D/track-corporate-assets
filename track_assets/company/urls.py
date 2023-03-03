from django.urls import path, include
from .views import *

urlpatterns = [
    path("", EmployeesView.as_view(), name="home"),
    path("add-employee/", add_employee, name="add_employee"),
    path("payment/", payment_getway, name="payment")
]
