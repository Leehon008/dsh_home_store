from django.db import models
from .orders import Order

class Revenue(models.Model):
    name = models.CharField(max_length=60)
    quantity= models.IntegerField(default=0)
    order= models.ForeignKey(Order,on_delete=models.CASCADE,default=1 )
    company= models.CharField(max_length=250, default='', blank=True, null= True)
    
    def __str__(self):
        return self.name
        
    @staticmethod
    def get_revenues_by_id(ids):
        return Revenue.objects.filter (id__in=ids)
    @staticmethod
    def get_all_revenues():
        return Revenue.objects.all()

    @staticmethod
    def get_all_revenues_by_order_id(order_id):
        if order_id:
            return Revenue.objects.filter (order=order_id)
        else:
            return Revenue.get_all_revenues();