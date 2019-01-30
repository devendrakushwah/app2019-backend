from django.urls import path
from .views import maintain
urlpatterns = [
    path('/',maintain),
]