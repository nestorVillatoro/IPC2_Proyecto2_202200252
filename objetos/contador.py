class datoContador:

    def __init__(self, nombre):
        self.Nombre = nombre
    
    def ObtenerNombre(self):
        return self.Nombre
    
    def EncontroNombre(self, Nombre):
        if self.Nombre == Nombre:
            return True
        return False