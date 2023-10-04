class NodoData:
    
    def __init__(self, dato):
        self.dato = dato
        self.Siguiente = None
    
    def AsignarSiguiente(self, valorsiguiente):
        self.Siguiente = valorsiguiente

    def ObtenerDato(self):
        return self.dato
    
    def CambiarDato(self, NuevoDato):
        self.dato = NuevoDato

class ListaMensajes:

    def __init__(self):
        self.Inicio=None
        self.Final=None
        self.Contador=0
    
    def Insertar(self, dato):
        NodoActual = NodoData(dato)
        self.Contador = self.Contador + 1
        if self.Inicio is None:
            self.Inicio = NodoActual
            self.Final = NodoActual
        else:
            self.Final.AsignarSiguiente(NodoActual)
            self.Final = NodoActual

    def Imprimir(self):
        auxiliar=self.Inicio
        while auxiliar!=None:
            instruccion=auxiliar.ObtenerDato()
            dron=instruccion.ObtenerDron()
            instruccion_dron=instruccion.ObtenerInstruccion()
            print("Dron: "+str(dron)+ " se mueve a : "+str(instruccion_dron))
            auxiliar=auxiliar.Siguiente

    def ImprimirColumna(self):
        auxiliar = self.Inicio
        pformamatriz = " "
        while auxiliar is not None:
            pformamatriz = pformamatriz +" "+str(auxiliar.ObtenerDato()) 
            auxiliar = auxiliar.Siguiente
        return pformamatriz


    def Ordenar(self):
        if not self.Inicio:
            return
        actual = self.Inicio
        while actual:
            siguiente = actual.Siguiente
            while siguiente:
                if actual.dato > siguiente.dato:
                    actual.dato, siguiente.dato = siguiente.dato, actual.dato
                siguiente = siguiente.Siguiente
            actual = actual.Siguiente