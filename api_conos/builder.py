class ConoBuilder:
    PRECIO_TOPPINGS = {
        "queso_extra": 1.5,
        "papas_al_hilo": 1.0,
        "salchicha_extra": 1.5,
        "huevo": 1.0,
        "salsa_picante": 0.5,
        "vegetales": 0.8,
    }
    MULTIPLICADOR_TAMANIO = {
        "Pequeño": 1.0,
        "Mediano": 1.2,
        "Grande": 1.5,
    }

    def __init__(self, base):
        self.base = base
        self.toppings = []
        self.tamanio = "Mediano"

    def agregar_toppings(self, lista):
        self.toppings.extend(lista)

    def definir_tamanio(self, tam):
        self.tamanio = tam

    def obtener_precio(self):
        base = self.base.precio_base()
        extras = sum(self.PRECIO_TOPPINGS.get(t, 0) for t in self.toppings)
        total = (base + extras) * self.MULTIPLICADOR_TAMANIO.get(self.tamanio, 1.0)
        return round(total, 2)

    def obtener_ingredientes_finales(self):
        return self.base.ingredientes_base() + self.toppings
