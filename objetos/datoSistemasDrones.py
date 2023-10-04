class datoSistemasDrones:
    def __init__(self, nombresistema, alturamaxima, cantidaddrones, sistemaDrones):
        self.nombresistema=nombresistema
        self.alturamaxima=alturamaxima
        self.cantidaddrones=cantidaddrones
        self.sistemaDrones=sistemaDrones

    def ObtenerNombreSistema(self):
        return self.nombresistema
    
    def ObtenerAlturaMaxima(self):
        return self.alturamaxima
    
    def ObtenerCantidadDrones(self):
        return self.cantidaddrones
    
    def ObtenerSistemaDrones(self):
        return self.sistemaDrones
    
