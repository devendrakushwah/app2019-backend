from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from api.urls import *
from maintain.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',include('api.urls')),
    path('maintain',include('maintain.urls')),
]
