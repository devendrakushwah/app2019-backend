from django.urls import path
from .views import *

app_name='maintain'

urlpatterns = [
    path('/',maintain,name='maintain'),
    path('/update_coins',update_coins,name='update_coins'),
    path('/update_news',update_news,name='update_news'),
    path('/update_exchange',update_exchange,name='update_exchanges'),
]