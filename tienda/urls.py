from django.urls import path
from .views import *

app_name = 'tienda'
urlpatterns = [
    path('', inicio, name='inicio' ),
]