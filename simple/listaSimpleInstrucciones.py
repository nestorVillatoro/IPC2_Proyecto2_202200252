class nodoSimpleInstrucciones:

    def __init__(self, Dato):
        self.Dato = Dato
        self.Siguiente = None

    
    def ObtenerNombre(self):
        return self.Dato.ObtenerNombre()
    
    def ObtenerIndice(self):
        return self.Dato.ObtenerAltura()
    
    def ObtenerSiguiente(self):
        return self.Siguiente
    
    def SetSiguiente(self, NodoS):
        self.Siguiente = NodoS

    def Buscar(self, Nombre):
        return self.Dato.EncontroNombre(Nombre)

class ListaSimpleInstrucciones:

    def __init__(self):
        self.Inicio = None
        self.Final = None

    def Insertar(self, Dato):
        NuevoNodo = nodoSimpleInstrucciones(Dato)

        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.SetSiguiente(NuevoNodo)
            self.Final = NuevoNodo

    def Pop(self):
        if self.Inicio != None:
            if self.Inicio.ObtenerSiguiente() == None:
                Auxiliar = self.Inicio
                self.Inicio = None
                self.Final = None
                return Auxiliar
            else:
                Auxiliar = self.Inicio
                self.Inicio = self.Inicio.ObtenerSiguiente()
                Auxiliar.SetSiguiente(None)
                return Auxiliar
            
    def EliminarIndice(self, indice):
        #indice será un valor numérico, que indica la posición de la lista a eliminar, la primera posición será 0
        if self.Inicio == None:
            print("La lista está vacía, no se puede eliminar nada.")
            return None
        if indice < 0:
            print("No se pueden eliminar posiciones menores a 0")
            return None
        if indice == 0:
            Auxiliar = self.Pop()
            return Auxiliar
        Auxiliar = self.Inicio
        Contador = 0
        Auxliar2 = None
        while Auxiliar != None:
            if Contador == indice:
                if Auxiliar == self.Final:
                    self.Final = Auxliar2
                Auxliar2.SetSiguiente(Auxiliar.ObtenerSiguiente())
                Auxiliar.SetSiguiente(None)
                print("Se eliminó la posicion requerida")
                return Auxiliar
            Auxliar2 = Auxiliar
            Auxiliar = Auxiliar.ObtenerSiguiente()
            Contador += 1
        print("No existe la posición indicada")
        return None
            
    def EliminarElemento(self, Nombre):
        #indice será un valor numérico, que indica la posición de la lista a eliminar, la primera posición será 0
        if self.Inicio == None:
            print("La lista está vacía, no se puede eliminar nada.")
            return None
        if self.Inicio.Buscar(Nombre):
            Auxiliar = self.Pop()
            return Auxiliar
        Auxiliar = self.Inicio
        Auxliar2 = None
        while Auxiliar != None:
            if Auxiliar.Buscar(Nombre):
                if Auxiliar == self.Final:
                    self.Final = Auxliar2
                Auxliar2.SetSiguiente(Auxiliar.ObtenerSiguiente())
                Auxiliar.SetSiguiente(None)
                print("Se eliminó el elemento solicitado")
                return Auxiliar
            Auxliar2 = Auxiliar
            Auxiliar = Auxiliar.ObtenerSiguiente()
        print("No existe el elemento con ese filtro.")
        return None
    
    def ImprimirElmentos(self):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                print("Nombre:",Auxiliar.ObtenerNombre(),"Indice:",Auxiliar.ObtenerIndice())
                Auxiliar = Auxiliar.ObtenerSiguiente()
        else:
            print("Lista Vacía")

    def obtenerElementos(self):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            elemento = ""
            contador = 0
            while Auxiliar != None:
                contador += 1
                elemento += str(contador) + " - Nombre: " + str(Auxiliar.ObtenerNombre()) + "\n"
                Auxiliar = Auxiliar.ObtenerSiguiente()
            return elemento

    
    def buscarElmentos(self, Nombre):
        if self.Inicio != None:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                if Auxiliar.ObtenerNombre() == Nombre:
                    return False
                Auxiliar = Auxiliar.ObtenerSiguiente()
            return True
        else:
            print("Lista Vacía")