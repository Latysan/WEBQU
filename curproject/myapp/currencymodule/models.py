from django.db import models

class currency_table(models.Model):

    curr = models.CharField(max_length=50, default='USD')
    value = models.FloatField(default = 0.0)
    Symbol =  models.CharField(max_length=3, default='$')
    
    curr_S = models.CharField(max_length=50, default='USD')

    
    
    def __str__(self):
        return self.curr

   
        