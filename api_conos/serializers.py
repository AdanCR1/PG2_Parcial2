from rest_framework import serializers
from .models import PedidoCono
from .factory import ConoFactory
from .builder import ConoBuilder
from api_patrones.logger import Logger

class PedidoConoSerializer(serializers.ModelSerializer):
    precio_final = serializers.SerializerMethodField()
    ingredientes_finales = serializers.SerializerMethodField()

    class Meta:
        model = PedidoCono
        fields = [
            'id', 'cliente', 'variante', 'toppings',
            'tamanio_cono', 'fecha_pedido',
            'precio_final', 'ingredientes_finales',
        ]

    def validate_toppings(self, value):
        validos = {
            "queso_extra", "papas_al_hilo", "salchicha_extra",
            "huevo", "salsa_picante", "vegetales"
        }
        if not isinstance(value, list):
            raise serializers.ValidationError("Los toppings deben estar en una lista.")
        invalidos = [t for t in value if t not in validos]
        if invalidos:
            raise serializers.ValidationError(f"Toppings inválidos: {invalidos}")
        return value

    def get_precio_final(self, obj):
        base = ConoFactory.obtener_cono(obj.variante)
        builder = ConoBuilder(base)
        builder.agregar_toppings(obj.toppings)
        builder.definir_tamanio(obj.tamanio_cono)
        total = builder.obtener_precio()
        Logger().registrar(f"Pedido {obj.id}: precio calculado {total}")
        return total

    def get_ingredientes_finales(self, obj):
        base = ConoFactory.obtener_cono(obj.variante)
        builder = ConoBuilder(base)
        builder.agregar_toppings(obj.toppings)
        builder.definir_tamanio(obj.tamanio_cono)
        Logger().registrar(f"Pedido {obj.id}: ingredientes listados")
        return builder.obtener_ingredientes_finales()
