from django.shortcuts import render

def index(request):
    return render(request,'currencymodule/welcome.html') 

def currency(request):
    
    return render(request,'currencymodule/currency.html',{'curr':exchanges()}) 

def exchanges():
    currency=[]
    C1 = {'currency':'Dollar',"Symbol":"$", 'value':0.27}
    C2 = {'currency':'Emirates Dirham',"Symbol":"د.إ", 'value':0.98}
    C3 = {'currency':'Qatari Riyal',"Symbol":"﷼", 'value':0.97}
    C4 = {'currency':'Chinese Yuan',"Symbol":"¥", 'value':1.91}
    C5 = {'currency':'Euro',"Symbol":"€", 'value':0.24}
    C6 = {'currency':'Iraqi Dinar',"Symbol":"د.ع", 'value':349.50}
    C7 = {'currency':'Turkish lira',"Symbol":"TL", 'value':8.58}
    C8 = {'currency':'Egyptian Pound',"Symbol":"£", 'value':13.06}
    C9 = {'currency':'Japanese Yen',"Symbol":"¥", 'value':39.29}
    C10 = {'currency':'Korean won',"Symbol":"₩", 'value':349.10}
    C11 = {'currency':'Kuwaiti Dinar',"Symbol":"ك", 'value':0.082}
    C12 = {'currency':'Bahraini_Dinar',"Symbol":"BD", 'value':0.10}

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

    
  