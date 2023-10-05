from .nodoColumnas import NodoColumnas

class Columna:
    
    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0
        
    def Insertar(self, dato):
        NodoActual = NodoColumnas(dato)
        self.Contador = self.Contador + 1
        if self.Inicio is None:
            self.Inicio = NodoActual
            self.Final = NodoActual
        else:
            NodoActual.AsignarAnterior(self.Final)
            self.Final.AsignarSiguiente(NodoActual)
            self.Final = NodoActual


    def ImprimirColumna(self):
        auxiliar = self.Inicio
        pformamatriz = " "
        while auxiliar is not None:
            pformamatriz = pformamatriz +" "+str(auxiliar.ObtenerDato()) 

            auxiliar = auxiliar.Siguiente
        return pformamatriz

    def BuscarValorenColumna(self, columna):
        Contador = 0
        auxiliar = self.Inicio
        if columna == 0 or columna > self.Contador:
            print("NO EXISTE LA COLUMNA")
            return
        else:
            while auxiliar is not None:
                Contador += 1
                if Contador == columna:
                    dato = auxiliar.ObtenerDato()
                    return dato
                auxiliar = auxiliar.Siguiente

    def Borrar(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0

    def DatosColumna(self):
        Auxiliar = self.Inicio
        datosColumna = ""
        while Auxiliar is not None:
            datoColumna = str(Auxiliar.ObtenerDato())
            datosColumna = datosColumna + datoColumna + ","
            Auxiliar = Auxiliar.Siguiente
        return datosColumna
