class datoInstruccionesDrones:

    def __init__(self, valor, nombre):
        self.Valor = valor
        self.Nombre = nombre

    def ObtenerValor(self):
        return self.Valor
    
    def ObtenerNombre(self):
        return self.Nombre
    
    def EncontroNombre(self, Nombre):
        if self.Nombre == Nombre:
            return True
        return False