from django.urls import path
from django.urls import include
from .views import *

urlpatterns = [
    path('', pizzes_list, name='pizzes_list_url'),
    path('create/', PizzaCreate.as_view(), name='pizza_create_url'),
    path('<str:slug>/', PizzaDetail.as_view(), name='pizza_detail_url'),
    path('<str:slug>/update/', PizzaUpdate.as_view(), name='pizza_update_url'),
    path('<str:slug>/delete/', PizzaDelete.as_view(), name='pizza_delete_url'),
    path('toping/create/', TopingCreate.as_view(), name='toping_create_url'),
    path('toping/<str:slug>/', TopingDetail.as_view(), name='toping_detail_url'),
    path('toping/<str:slug>/update/', TopingUpdate.as_view(), name='toping_update_url'),
    path('toping/<str:slug>/delete/', TopingDelete.as_view(), name='toping_delete_url'),
]
