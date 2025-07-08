from .base import ConoCarnivoro, ConoVegetariano, ConoSaludable

class ConoFactory:
    @staticmethod
    def obtener_cono(variante):
        opciones = {
            "Carnívoro": ConoCarnivoro,
            "Vegetariano": ConoVegetariano,
            "Saludable": ConoSaludable,
        }
        cls = opciones.get(variante)
        if not cls:
            raise ValueError("Variante de cono no válida")
        instancia = cls()
        instancia.inicializar()
        return instancia
