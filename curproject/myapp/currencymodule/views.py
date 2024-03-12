from django.shortcuts import render

def index(request):
    return render(request,'currencymodule/welcome.html') 

def currency(request):
    return render(request,'currencymodule/currency.html') 