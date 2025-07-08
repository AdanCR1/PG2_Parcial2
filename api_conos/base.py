class ConoBase:
    def __init__(self):
        self.base = None
    def inicializar(self):
        raise NotImplementedError
    def precio_base(self):
        raise NotImplementedError
    def ingredientes_base(self):
        raise NotImplementedError

class ConoCarnivoro(ConoBase):
    def inicializar(self):
        self.base = "Carne + Queso"
    def precio_base(self):
        return 5.0
    def ingredientes_base(self):
        return ["carne", "queso"]

class ConoVegetariano(ConoBase):
    def inicializar(self):
        self.base = "Vegetales"
    def precio_base(self):
        return 4.0
    def ingredientes_base(self):
        return ["vegetales"]

class ConoSaludable(ConoBase):
    def inicializar(self):
        self.base = "Ensalada ligera"
    def precio_base(self):
        return 4.5
    def ingredientes_base(self):
        return ["ensalada"]
