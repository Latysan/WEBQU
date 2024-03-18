from django.shortcuts import render

def index(request):
    return render(request,'currencymodule/welcome.html') 

def currency(request):
    
    return render(request,'currencymodule/currency.html',{'curr':exchanges()}) 

def exchanges():
    currency=[]
    C1 = {'currency':'Dollar', 'value':0.27}
    C2 = {'currency':'Emirates Dirham', 'value':0.98}
    C3 = {'currency':'Qatari Riyal', 'value':0.97}
    C4 = {'currency':'Chinese Yuan', 'value':1.91}
    C5 = {'currency':'Euro', 'value':0.24}
    C6 = {'currency':'Iraqi Dinar', 'value':349.50}
    C7 = {'currency':'Hong Kong Dolla', 'value':2.09}
    C8 = {'currency':'Egyptian Poun', 'value':13.06}
    C9 = {'currency':'Japanese Yen', 'value':39.29}
    C10 = {'currency':'Korean won', 'value':349.10}
    C11 = {'currency':'Kuwaiti Dinar', 'value':0.082}
    C12 = {'currency':'Bahraini_Dinar', 'value':0.10}

    currency.append(C1)
    currency.append(C2)
    currency.append(C3)
    currency.append(C4)
    currency.append(C5)
    currency.append(C6)
    currency.append(C7)
    currency.append(C8)
    currency.append(C9)
    currency.append(C10)
    currency.append(C11)
    currency.append(C12)
    
    return currency

def converter(request):
    
    return render(request,'currencymodule/converter.html') 

    
  