from django.urls import path
from maintain.views import maintain
urlpatterns = [
    path('/',maintain),
]