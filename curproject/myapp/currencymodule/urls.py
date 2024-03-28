from django.urls import path
from myapp.currencymodule import views
from django.conf import settings


urlpatterns = [    
     path('',views.index, name="index"),
     path('exchange',views.currency,name="currency"),
     path('convert',views.converter,),
] 