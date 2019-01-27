from django.db import models

# Create your models here.

#Model to handle all the image URLs
class Image(models.Model):
    symbol=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=200)
    url=models.URLField()

    def __str__(self):
        return self.name


#Model to store values of different currencies against USD
class Exchange(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    value=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Coin(models.Model):
    id=models.IntegerField(max_length=10)
    cmc_rank=models.IntegerField(max_length=10)
    symbol = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    price_usd = models.CharField(max_length=200)
    total_supply = models.CharField(max_length=200)
    max_supply = models.CharField(max_length=200)
    circulating_supply = models.CharField(max_length=200)
    change_hour = models.CharField(max_length=200)
    change_day = models.CharField(max_length=200)
    change_week = models.CharField(max_length=200)
    last_update = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)+' '+str(self.name)