from django.urls import path
from .views import PedidoConoCreateView, PedidoConoListView

urlpatterns = [
    path('pedidos_conos/', PedidoConoListView.as_view(), name='listar-conos'),
    path('pedidos_conos/crear/', PedidoConoCreateView.as_view(), name='crear-cono'),
]
