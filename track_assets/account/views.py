from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import *
# Create your views here.


def SignUp(request):
    forms = SignUpForm()
    try:
        if request.method == "POST":
            forms = SignUpForm(request.POST)
            if forms.is_valid():
                forms.save()
                # userForm = forms.save()
                # profile = Profile.objects.create(user = userForm)
                # profile.save()
                # userForm.save()
                messages.success(request, 'Account Created Successfully!!')
                return HttpResponseRedirect(request.path_info)
        else:
            forms = SignUpForm()
    except Exception as e:
        print(e)

    context = {
        forms: 'forms'
    }
    return render(request, 'account/signup.html', context)
