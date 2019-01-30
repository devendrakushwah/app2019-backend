from django.contrib import admin
from api.models import Image,Coin,Exchange,News
# Register your models here.
admin.site.register(Image)
admin.site.register(Coin)
admin.site.register(Exchange)
admin.site.register(News)