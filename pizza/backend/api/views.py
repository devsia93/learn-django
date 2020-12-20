from rest_framework.viewsets import ModelViewSet

from .serializers import *


class PizzaViewSet(ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
