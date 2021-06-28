from django.db import models

# Create your models here.
class TradeDetail(models.Model):
    class Meta:
        db_table = 'TradeDetail'
        
    id = models.IntegerField(primary_key=True)
    stock_num = models.CharField(max_length=20)
    brokerage_name = models.CharField(max_length=20)
    date = models.DateTimeField()
    total = models.FloatField()
    buy_avg = models.FloatField()
    buy_quantity = models.IntegerField()
    sell_avg = models.FloatField()
    sell_quantity = models.IntegerField()


class TraceList(models.Model):
    class Meta:
        db_table = 'TraceList'
        
    stock_num = models.CharField(primary_key=True, max_length=20)
    stock_name = models.CharField(max_length=20)
