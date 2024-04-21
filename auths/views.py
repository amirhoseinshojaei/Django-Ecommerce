from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import RegistrationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
# Create your views here.

def signup_view(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            messages.success(request,f'Hey {username} Your account was successful created')
            new_user = authenticate(username=email,password=password)
            login(request,new_user)
            return redirect("web:home") # ToDo; After create web app and home page , edit this
    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request,'auths/registration/signup.html',context)
