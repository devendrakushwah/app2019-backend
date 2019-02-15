from django.urls import re_path,path
from api.views import *
urlpatterns = [
    path('/',get_top_coins),
    path('/get_top_coins/',get_top_coins),
    path('/get_details/',get_details),
    path('/search_coins/',search_coins),
    path('/get_news/',get_news),
    path('/get_currency_list/',get_currency_list),
]