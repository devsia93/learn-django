from django.urls import path

from .views import *


app_name = 'flight'

urlpatterns = [
    path('', airports, name='airports'),
    path('<int:id_flight>', flight, name="flight"),
    path('date_filter/', date_filter, name='date_filter'),
]