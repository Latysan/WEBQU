from django.shortcuts import render
from .models import currency_table


def index(request):
    return render(request,'currencymodule/welcome.html') 

def currency(request):
    
     
    
     if request.method == "POST":
        selected_currency = request.POST.get('curr')
        filtered_currencies =currency_table.objects.filter(curr=selected_currency)
        return render(request, 'currencymodule/exchange.html', {'infos': filtered_currencies}) 
     else:
        display = currency_table.objects.all().order_by('value')
        return render(request, 'currencymodule/exchange.html', {'infos': display})

    
    


def converter(request):
    display=currency_table.objects.all()
    return render(request,'currencymodule/converter.html', {'infos': display}) 

    
  