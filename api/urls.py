from django.urls import re_path,path
from api.views import *
urlpatterns = [
    path('/',get_top_coins),
    path('/get_top_coins/',get_top_coins),
    path('/get_details/',get_details),
]