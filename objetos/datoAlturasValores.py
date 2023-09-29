class datoAlturasValores:

    def __init__(self, valor, nombre, indice):
        self.Valor = valor
        self.Nombre = nombre
        self.Indice = indice

    def ObtenerValor(self):
        return self.Valor
    
    def ObtenerNombre(self):
        return self.Nombre
    
    def ObtenerIndice(self):
        return self.Indice
    
    def EncontroNombre(self, Nombre):
        if self.Nombre == Nombre:
            return True
        return False