from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import RegistrationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def signup_view(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            form.save()
            messages.success(request,f'Hey {username} Your account was successful created')
            new_user = authenticate(username=email,password=password)
            login(request,new_user)
            return redirect("web:home") # ToDo; After create web app and home page , edit this
    else:
        form = RegistrationForm()

    context = {'form':form}
    return render(request,'auths/registration/signup.html',context)

def login_view(request):

    if request.user.is_authenticated:
        messages.warning(request,"Hey You are already LoggedIn")
        # return redirect("web:index")

    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            CustomUser.objects.get(email = email)
            user = authenticate(request,email=email , password = password)

            if user is not None:
                login (request, user)
                messages.success(request,"You are LoggedIn")
                # return redirect('web:index')
            else:
                messages.warning(request,'User Does not exist create an account')

        except:
            messages.warning(request,f'User with {email} Does Not Exist')



    return render(request,'auths/registration/login.html')


def logout_view(request):
    logout(request)
    messages.success(request,"You are Logged Out")
    return redirect('auths:sign-in')