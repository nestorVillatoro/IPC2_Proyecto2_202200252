class NodoSistema:
    def __init__(self, sistema):
        self.sistema = sistema
        self.siguiente = None

class ListaSistemas:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0
                
    def Insertar(self, sistema):
        NuevoNodo = NodoSistema(sistema)
        self.Contador = self.Contador+1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.siguiente=NuevoNodo
            self.Final = NuevoNodo

    def ImprimirSistemas(self):
        Auxiliar = self.Inicio
        while Auxiliar is not None:
            sistema = Auxiliar.sistema
            print("Nombre del sistema:", sistema.nombresistema)
            print("Altura máxima:", sistema.alturamaxima)
            print("Cantidad de drones:", sistema.cantidaddrones)
            sistema.sistemaDrones.ImprimirMatriz()
            print("\n")
            Auxiliar = Auxiliar.siguiente
    
    def InicializarSistema(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0

    def ObtenerSistemas(self):
        Auxiliar = self.Inicio
        while Auxiliar is not None:
            sistema = Auxiliar.sistema
            print("Nombre del sistema:", sistema.nombresistema)
            print("Altura máxima:", sistema.alturamaxima)
            print("Cantidad de drones:", sistema.cantidaddrones)
            sistema.sistemaDrones.ImprimirMatriz()
            print("\n")
            Auxiliar = Auxiliar.siguiente
