from django.urls import path
from myapp.currencymodule import views

urlpatterns = [    
     path('',views.index, name="index"),
     path('exchange',views.currency,name="currency"),
]