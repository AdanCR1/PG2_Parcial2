from rest_framework import generics
from .models import PedidoCono
from .serializers import PedidoConoSerializer

class PedidoConoCreateView(generics.CreateAPIView):
    queryset = PedidoCono.objects.all()
    serializer_class = PedidoConoSerializer

class PedidoConoListView(generics.ListAPIView):
    queryset = PedidoCono.objects.all()
    serializer_class = PedidoConoSerializer