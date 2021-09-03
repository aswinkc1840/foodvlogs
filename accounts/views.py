from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"USERNAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"EMAIL TAKEN")
                return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password1,email=email,first_name=fname,last_name=lname)
                user.save();
                print("user created")

        else:
            print("PASSWORD NOT MATCH")
            return redirect('register')

        return redirect('/')

    else:
      return  render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"INVALID DETAILS")
            return redirect('login')
    else:
        return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return  redirect('/')

