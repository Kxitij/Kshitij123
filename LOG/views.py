from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import views
# Create your views here.
def home(request):
    return render(request, "LOG/index.html")

def signup(request):
    if request.method == "POST":
        usn = request.POST['USN']
        sem = request.POST['sem']
        dept = request.POST['dept']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1==pass2:
            student= User.objects.create_user(usn,email,pass1)
            student.first_name = fname
            student.last_name = lname
            student.save()
            messages.success(request, "Account created succesfully!!")

        return redirect('signin')



    return render(request, "LOG/signup.html")

def signin(request):
    if request.method == "POST":
        usn = request.POST['USN']
        pass1 = request.POST['pass1']
        lab = request.POST['lab']

        user = authenticate(usn=usn,password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request, "LOG/index.html", {'fname': fname})

        else: 
            messages.error(request,"Invalid Credentials")
            return redirect('home')


    return render(request, "LOG/signin.html")

def signout(request):
    return redirect('home')

