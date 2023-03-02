from django.http import HttpResponseRedirect ,HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm


# Create your views here.
def signup(request):
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
    context = {'forms': forms}
    

    return render(request, 'account/signup.html', context)



def login_page(request):
        # if request.user.is_authenticated:
        #     return redirect('index')
       
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username)
        
        if not user_obj.exists():
            messages.warning(request, 'Account not Found')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = username, password = password)

        if user_obj is not None:
            login(request, user_obj)
            # username = User.username
            return redirect('home')
        else:
            messages.warning(request, 'Username or password is not correct')
            return HttpResponseRedirect(request.path_info)
    
        # messages.warning(request, 'Invalid Information')
        # context = { 'username': username}
    else:
        if request.user.is_superuser == True:
            messages.warning(request, 'Admin user can not login')
        
    return render(request, 'account/login.html')
