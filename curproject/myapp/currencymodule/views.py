from itertools import count
from django.shortcuts import render
from .models import currency_table
from django.db.models import Q
from django.db.models import Count
from .forms import InputForm, OutputForm




def index(request):
    return render(request,'currencyModule/welcome.html') 

def currency(request):
    
     
    
     if request.method == "POST":
        selected_currency = request.POST.get('options')
        filtered_currencies =currency_table.objects.filter(curr=selected_currency)
        return render(request, 'currencyModule/exchange.html', {'infos': filtered_currencies}) 
     else:
        display = currency_table.objects.annotate(total_value=Count('value', filter=Q(value__gte=1)))
        
       # display = currency_table.objects.all().order_by('value')
        return render(request, 'currencyModule/exchange.html', {'infos': display})





def converter(request):

        input_form = InputForm()
        output_form = OutputForm()
        return render(request, 'currencymodule/converter.html', {'input_form': input_form, 'output_form': output_form})

    
  
#filtered_objects = currency_table.objects.filter(Q(value__gte=1))
