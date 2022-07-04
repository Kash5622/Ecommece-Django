from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from collections import namedtuple
from django.contrib import messages
from django.contrib.auth.models import User, auth
from shoptop.models import product


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            mydata = product.objects.all()
            context = {
                'members': mydata,
            }
            return render(request, 'shop/index.html', context)
        else:
            messages.info(request,"Wrong credentials")
            return redirect('/account/login')
    else:
        return render(request, 'shop/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,"User name already taken")
                return redirect('/account/register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email already taken")
                return redirect('/account/register')
            else:
                print("")
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                print("created")
                return redirect('/account/login')

        else:
            messages.info(request,"Password did not matched")
            return redirect('/account/register')

    else:
        return render(request, 'shop/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')