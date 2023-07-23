from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'mpesa/home.html')

def customers(request):
    return render(request, 'mpesa/customers.html')
