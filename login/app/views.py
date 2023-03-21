from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_Password = request.POST['confirm password']
        if password == confirm_Password:
            if User.objects.filter(username == username).exists():
                messages.info("username exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, firstname=firstname, lastname=lastname, email=email, password=password)

                user.save();
                return redirect('login')
        else:
            messages.info(request, "password does not match")
            return redirect('register')
    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password not correct')
            return redirect('login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')