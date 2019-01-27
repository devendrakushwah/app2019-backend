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