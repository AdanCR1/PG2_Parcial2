class Logger:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super().__new__(cls)
            cls._instancia.logs = []
        return cls._instancia

    def registrar(self, mensaje):
        self.logs.append(mensaje)

    def mostrar_logs(self):
        return self.logs
