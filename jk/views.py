from django.shortcuts import render
from . models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password = request.POST.get("password")
        if (Registration.objects.filter(Username=username, Password=password).exists()):
            regs = Registration.objects.filter(Username=username, Password=password)
            for value in regs:
                firstname=value.First_name
                lastname=value.Last_name
                return render(request,'index.html',{'firstname' :firstname})
    return render(request,'login.html')


def index(request):
    a = Product.objects.all()
    return render(request,'index.html',{'a':a})

def registration(request):
    if request.method=='POST':
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        username=request.POST.get("username")
        password = request.POST.get("password")
        reg=Registration()
        reg.First_name = firstname
        reg.Last_name = lastname
        reg.Username = username
        reg.Password = password
        reg.save()
        return render(request,'index.html')

    return render(request,'registration.html')

def category_fruits(request):
    fruits = Product.objects.filter(Product_category = 'fruit')
    return render(request,'category_fruits.html',{'fruits':fruits})

def category_vegetables(request):
    vegetables = Product.objects.filter(Product_category = 'vegetable')
    return render(request,'category_vegetables.html',{'vegetables':vegetables})