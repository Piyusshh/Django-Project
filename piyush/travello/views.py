from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Destination
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            #if User.objects.create_user(username=username).exists():
            #    messages.info(request,'Username Taken')
            #    print('Username already Taken')
            #    return redirect('travello:register')
            #elif User.objects.filter(email=email).exists():
            #    messages.info(request, 'Email Already exists')
            #    print('Email Already Exists')
            #    return redirect('travello:register')
            #else:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print('user created')
        else:
            print('Password not matching...')
            messages.info(request, 'Password Not Matching')
            print('Password Not Matching')
            return redirect('travello:register')
        return redirect('travello:index')
        #return HttpResponse("Registered Successfull ! ")
    else:
        return render(request, 'register.html')
