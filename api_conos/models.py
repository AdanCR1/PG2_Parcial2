from django.db import models
from django.core.exceptions import ValidationError

class PedidoCono(models.Model):
    VARIANTES = [
        ("Carnívoro", "Carnívoro"),
        ("Vegetariano", "Vegetariano"),
        ("Saludable", "Saludable"),
    ]
    TAMANIOS = [
        ("Pequeño", "Pequeño"),
        ("Mediano", "Mediano"),
        ("Grande", "Grande"),
    ]

    cliente = models.CharField(max_length=100)
    variante = models.CharField(max_length=20, choices=VARIANTES)
    toppings = models.JSONField(default=list, blank=True, help_text="queso_extra, papas_al_hilo, salchicha_extra, huevo, salsa_picante, vegetales")
    tamanio_cono = models.CharField(max_length=10, choices=TAMANIOS)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def clean(self):
        toppings_validos = {
            "queso_extra", "papas_al_hilo", "salchicha_extra",
            "huevo", "salsa_picante", "vegetales"
        }
        if not isinstance(self.toppings, list):
            raise ValidationError({"toppings": "Debe ser una lista."})
        for topping in self.toppings:
            if topping not in toppings_validos:
                raise ValidationError({"toppings": f"Topping inválido: {topping}"})

    def __str__(self):
        return f"{self.cliente} – {self.variante} ({self.tamanio_cono})"