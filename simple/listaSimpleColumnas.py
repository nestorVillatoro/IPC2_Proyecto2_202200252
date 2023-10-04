class nodoSimpleColumna:
    def __init__(self, dron):
        self.dron = dron
        self.siguiente = None

    def ObtenerNombre(self):
        return self.dron.ObtenerNombre()
    
    def ObtenerColumna(self):
        return self.dron.ObtenerColumna()

class ListaSimpleColumnas:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0
                
    def Insertar(self, dron):
        NuevoNodo = nodoSimpleColumna(dron)
        self.Contador = self.Contador+1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.siguiente=NuevoNodo
            self.Final = NuevoNodo

    def ImprimirMatriz(self):
        Auxiliar = self.Inicio
        while Auxiliar is not None:
            dron = Auxiliar.dron
            print(str(dron.nombre))
            dron.imprimirInstrucciones()
            print("\n")
            Auxiliar = Auxiliar.siguiente

    def obtenerMatriz(self):
        Auxiliar = self.Inicio
        while Auxiliar is not None:
            dron = Auxiliar.dron
            print(str(dron.nombre))
            dron.imprimirInstrucciones()
            print("\n")
            Auxiliar = Auxiliar.siguiente