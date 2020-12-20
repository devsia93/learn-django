from rest_framework import routers
from .views import PizzaViewSet

project_router = routers.DefaultRouter()

project_router.register(r'pizzes', PizzaViewSet)

urlpatterns = [
    *project_router.urls,
]
