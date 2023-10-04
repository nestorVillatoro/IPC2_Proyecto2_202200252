class NodoMensajes:

    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.Siguiente = None
    
    def AsignarSiguiente(self, valorsiguiente):
        self.Siguiente = valorsiguiente

    def ObtenerDato(self):
        return self.dato
    
    def CambiarDato(self, NuevoDato):
        self.dato = NuevoDato

class ListaInstrucciones:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0
                
    def Insertar(self, mensaje):
        NuevoNodo = NodoMensajes(mensaje)
        self.Contador = self.Contador+1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.siguiente=NuevoNodo
            self.Final = NuevoNodo 
    

    def ImprimirMensajes(self):
        Auxiliar = self.Inicio
        while Auxiliar is not None:
            mensaje = Auxiliar.mensaje
            print("Nombre mensaje:", mensaje.nombre_intruccion)
            print("Sistema:", mensaje.sistema_usar)
            print("Instrucciones:")
            mensaje.instrucciones.Imprimir()  
            print("\n")
            Auxiliar=Auxiliar.Siguiente

    def InicializarSistema(self):
        self.Inicio = None
        self.Final = None
        self.Contador = 0

    