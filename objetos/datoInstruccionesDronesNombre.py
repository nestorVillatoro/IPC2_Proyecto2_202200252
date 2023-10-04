class datoInstruccionesDronesNombre:

    def __init__(self, nombre, columna):
        self.nombre=nombre
        self.columna=columna

    def ObtenerNombre(self):
        return self.nombre
    
    def ObtenerColumna(self):
        return self.columna

    def imprimirInstrucciones(self):
        print(str(self.columna.ImprimirColumna()))

    def obtenerInstrucciones(self):
        return(str((self.columna.DatosColumna())))