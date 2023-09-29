class datoInstruccionesDronesNombre:

    def __init__(self, lista, nombre):
        self.Lista = lista
        self.Nombre = nombre

    def ObtenerLista(self):
        return self.Lista
    
    def ObtenerNombre(self):
        return self.Nombre
    
    def EncontroNombre(self, Nombre):
        if self.Nombre == Nombre:
            return True
        return False