from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User



def index(request):
    return render(request,'index.html')

# def signup_button(request):
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('store:base')
        else:
            messages.info(request, 'invalid user')
            return redirect('store:login')
    return render(request, "login.html" )


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('store:signup')
            elif User.objects.filter(password=password).exists():
                messages.info(request, 'pass already taken')
                return redirect('store:signup')
            if not username or not password or not cpassword:
                error_message='all fields are required!'
                return render(request,'signup.html',{'error_message':error_message})
            else:

                user = User.objects.create_user(username=username,
                                                 password=password)
                user.save()
                return redirect('store:login')
        else:
            messages.info(request, 'password not matching')
            return redirect('store:signup')
        # return redirect('/')
    return render(request, "signup.html")
def profile(request):
    # return redirect('store:index')


    return render(request,'profile.html')

def base(request):
    return render(request,'base.html')
def logout(request):
    auth.logout(request)
    # return redirect('store:index')
    return render(request,'index.html')
