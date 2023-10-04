class NodoColumnas:
    
    def __init__(self, dato):
        self.dato = dato
        self.Siguiente = None
        self.Anterior=None
    
    def AsignarSiguiente(self, valorsiguiente):
        self.Siguiente = valorsiguiente

    def AsignarAnterior(self, valoranterior):
        self.Anterior = valoranterior

    def ObtenerDato(self):
        return self.dato
    
    def CambiarDato(self, NuevoDato):
        self.dato = NuevoDato