from django.contrib import admin
from .models import PedidoCono

@admin.register(PedidoCono)
class PedidoConoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'variante', 'tamanio_cono', 'fecha_pedido')
    list_filter = ('variante', 'tamanio_cono',)
    search_fields = ('cliente',)
