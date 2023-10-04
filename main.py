import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import xml.etree.ElementTree as ET
import simple.listaSistemas as listaSistemas
import simple.listaMensajes as listaMensajes
import doble.lista_de_columna as lista_de_columna
import simple.listaSimple as listaSimple
import simple.listaSimpleInstrucciones as listaSimpleInstrucciones
import simple.listaSimpleColumnas as listaSimpleColumnas
import simple.listaInstrucciones as listaInstrucciones
import objetos.datoDron as datoDron
import objetos.datoSistemaDronesNombre as datoSistemaDronesNombre
import objetos.datoAlturasMaximas as datoAlturasMaximas
import objetos.datoCantidadDrones as datoCantidadDrones
import objetos.datoDronesdelSistema as datoDronesdelSistema
import objetos.datoMensajesNombres as datoMensajesNombres
import objetos.datoMensaje as datoMensaje
import objetos.datoMensajesSistemaDrones as datoMensajesSistemaDrones
import objetos.datoInstruccionesDronesNombre as datoInstruccionesDronesNombre
import objetos.datoMensajesInstrucciones as datoMensajesInstrucciones
import objetos.datoInstrucciones as datoInstrucciones
import objetos.contador as datoContador
import objetos.datoSistemasDrones as datoSistemasDrones
import objetos.datoAlturasValores as datoAlturasValores
from tkinter import filedialog, messagebox
from tkinter import Toplevel
import os

global listaDrones
listaDrones = None
global contadorDrones
contadorDrones = 0

global listaSistemaDronesNombre
listaSistemaDrones = None
global contadorSistemaDronesNombre
contadorSistemaDronesNombre = 0

global listaAlturasMaximas
listaAlturasMaximas = None
global contadorAlturasMaximas
contadorAlturasMaximas = 0

global listaCantidadDrones
listaCantidadDrones = None
global contadorCantidadDrones
contadorCantidadDrones = 0

global listaDronesdelSistema
listaDronesdelSistema = None
global contadorDronesdelSistema
contadorDronesdelSistema = 0

global listaAlturasValores
listaAlturasValores = None
global contadorAlturasValores
contadorAlturasValores = 0

global listaMensajesNombres
listaMensajesNombres = None
global contadorMensajesNombres
contadorMensajesNombres = 0

global listaMensajesSistemaDrones
listaMensajesSistemaDrones = None
global contadorMensajesSistemaDrones
contadorMensajesSistemaDrones = 0

global listaMensajesInstrucciones
listaMensajesInstrucciones = None
global contadorMensajesInstrucciones
contadorMensajesInstrucciones = 0

global listaInst
listaInst = listaInstrucciones.ListaInstrucciones()

global listaMensajesInstrucciones2
listaMensajesInstrucciones2 = None

global listaDobleInstruccionesDrones 
listaDobleInstruccionesDrones = None

global listaInstruccionesDronesNombre
listaInstruccionesDronesNombre = None

global listaSistemasD
listaSistemasD = listaSistemas.ListaSistemas()

global listaCantInstrucciones
listaCantInstrucciones = None

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")

        self.line_number_bar = tk.Text(root, width=4, padx=4, takefocus=0, border=0, background='lightgrey', state='disabled')
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        self.text_widget = ScrolledText(self.root, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill='both')

        self.text_widget.bind('<Key>', self.update_line_numbers)
        self.text_widget.bind('<MouseWheel>', self.update_line_numbers)

        self.current_line = 1

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        #____________________________________________________________________________
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="XML", menu=self.file_menu)
        self.file_menu.add_command(label="Cargar un archivo", command=self.cargarArchivo)
        self.file_menu.add_command(label="Generar un archivo", command=self.generarArchivo)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)

        self.menu_bar.add_cascade(label="Drones", menu=self.file_menu)
        self.file_menu.add_command(label="Lista de drones", command=self.listaDrones)
        self.file_menu.add_command(label="Agregar un dron", command=self.agregarDron)
        self.file_menu.add_separator()

        self.file_menu.add_command(label="Sistemas de drones", command=self.sistemaDrones)
        self.menu_bar.add_command(label="Inicializar", command=self.inicializar)
        self.menu_bar.add_command(label="Ayuda", command=self.ayuda)

    global verificador 
    verificador= False
    def cargarArchivo(self):
        global file_path
        global verificador
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.xml")])
        verificador = True
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.data = content
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
            self.update_line_numbers()
        self.data = self.text_widget.get(1.0, tk.END)

        archivo = ET.parse(file_path)
        raiz = archivo.getroot()
        global listaDrones
        listaDrones = listaSimple.ListaSimple()
        global contadorDrones

        global listaSistemaDronesNombre
        listaSistemaDronesNombre = listaSimple.ListaSimple()
        global contadorSistemaDronesNombre

        global listaAlturasMaximas
        listaAlturasMaximas = listaSimple.ListaSimple()
        global contadorAlturasMaximas
        
        global listaCantidadDrones
        listaCantidadDrones = listaSimple.ListaSimple()
        global contadorCantidadDrones

        global listaDronesdelSistema
        listaDronesdelSistema = listaSimple.ListaSimple()
        global contadorDronesdelSistema

        global listaAlturasValores
        listaAlturasValores = listaSimple.ListaSimple()
        global contadorAlturasValores

        global listaMensajesNombres
        listaMensajesNombres = listaSimple.ListaSimple()
        global contadorMensajesNombres

        global listaMensajesSistemaDrones
        listaMensajesSistemaDrones = listaSimple.ListaSimple()
        global contadorMensajesSistemaDrones

        global listaMensajesInstrucciones
        listaMensajesInstrucciones = listaSimpleInstrucciones.ListaSimpleInstrucciones()
        global contadorMensajesInstrucciones

        global listaMensajesInstrucciones2
        listaMensajesInstrucciones2 = listaSimple.ListaSimple()

        global listaCantInstrucciones
        listaCantInstrucciones = listaSimple.ListaSimple()

        for elementos in raiz:
            for drones in elementos.findall("dron"):
                contadorDrones += 1
                nombreDron = str(drones.text)
                Dron = datoDron.datoDron(nombreDron, contadorDrones)
                listaDrones.Insertar(Dron)
            for sistemaDrones in elementos.findall("sistemaDrones"):
                contadorSistemaDronesNombre += 1
                nombreSistema = str(sistemaDrones.get("nombre"))
                SistemaDronesNombre = datoSistemaDronesNombre.datoSistemaDronesNombre(nombreSistema, contadorSistemaDronesNombre)
                listaSistemaDronesNombre.Insertar(SistemaDronesNombre)
                for alturaMaxima in sistemaDrones.findall("alturaMaxima"):
                    contadorAlturasMaximas += 1
                    altura = str(alturaMaxima.text)
                    AlturasMaximas = datoAlturasMaximas.datoAlturasMaximas(altura, contadorAlturasMaximas)
                    listaAlturasMaximas.Insertar(AlturasMaximas)
                for cantidadDrones in sistemaDrones.findall("cantidadDrones"):
                    contadorCantidadDrones += 1
                    cantidad = str(cantidadDrones.text)
                    CantidadDrones = datoCantidadDrones.datoCantidadDrones(cantidad, contadorCantidadDrones)
                    listaCantidadDrones.Insertar(CantidadDrones)
                for contenido in sistemaDrones.findall("contenido"):
                    for dronesSistema in contenido.findall("dron"):
                        contadorDronesdelSistema += 1
                        nombreDrones = str(dronesSistema.text)
                        DronesdelSistema = datoDronesdelSistema.datoDronesdelSistema(nombreDrones, contadorDronesdelSistema)
                        listaDronesdelSistema.Insertar(DronesdelSistema)
                    for alturas in contenido.findall("alturas"):
                        for alturaSistema in alturas.findall("altura"):
                            contadorAlturasValores += 1
                            valor = str(alturaSistema.get("valor"))
                            alturaValor = str(alturaSistema.text)
                            AlturasValores = datoAlturasValores.datoAlturasValores(valor, alturaValor, contadorAlturasValores)
                            listaAlturasValores.Insertar(AlturasValores)
            for Mensaje in  elementos.findall("Mensaje"):
                contadorMensajesNombres += 1
                nombreMensaje = str(Mensaje.get("nombre"))
                MensajesNombres = datoMensajesNombres.datoMensajesNombres(nombreMensaje, contadorMensajesNombres)
                listaMensajesNombres.Insertar(MensajesNombres)
                for sistemadeDrones in  Mensaje.findall("sistemaDrones"):
                    contadorMensajesSistemaDrones += 1
                    sistema = str(sistemadeDrones.text)
                    MensajesSistemaDrones = datoMensajesSistemaDrones.datoMensajesSistemaDrones(sistema, contadorMensajesSistemaDrones)
                    listaMensajesSistemaDrones.Insertar(MensajesSistemaDrones)
                for instrucciones in  Mensaje.findall("instrucciones"):
                    contador = 0
                    for instruccion in instrucciones.findall("instruccion"):
                        contador += 1
                        contadorMensajesInstrucciones += 1
                        dron = str(instruccion.get("dron"))
                        alturaDron = str(instruccion.text)
                        MensajesInstrucciones = datoMensajesInstrucciones.datoMensajesInstrucciones(dron, contadorMensajesInstrucciones)
                        MensajesInstrucciones2 = datoMensajesInstrucciones.datoMensajesInstrucciones(alturaDron, contadorMensajesInstrucciones)
                        listaMensajesInstrucciones.Insertar(MensajesInstrucciones)
                        listaMensajesInstrucciones2.Insertar(MensajesInstrucciones2)
                    elContador = datoContador.datoContador(contador)
                    listaCantInstrucciones.Insertar(elContador)
        print("listaDrones:")
        listaDrones.ImprimirElmentos()
        print("\nlistaSistemaDronesNombre:")
        listaSistemaDronesNombre.ImprimirElmentos()
        print("\nlistaAlturasMaximas:")
        listaAlturasMaximas.ImprimirElmentos()
        print("\nlistaCantidadDrones:")
        listaCantidadDrones.ImprimirElmentos()
        print("\nlistaDronesdelSistema:")
        listaDronesdelSistema.ImprimirElmentos()
        print("\nlistaAlturasValores:")
        listaAlturasValores.ImprimirElmentos()
        print("\nlistaMensajesNombres:")
        listaMensajesNombres.ImprimirElmentos()
        print("\nlistaMensajesSistemaDrones:")
        listaMensajesSistemaDrones.ImprimirElmentos()
        print("\n")
        


        global listaDobleInstruccionesDrones
        global listaInstruccionesDronesNombre
        global listaSistemasD
        global listaInst 
        for i in range(contadorSistemaDronesNombre):
            var1 = int(listaAlturasMaximas.Pop().ObtenerNombre())
            var2 = int(listaCantidadDrones.Pop().ObtenerNombre())
            nombreSistema = listaSistemaDronesNombre.Pop().ObtenerNombre()
            listaInstruccionesDronesNombre = listaSimpleColumnas.ListaSimpleColumnas()
            for k in range(var2):    
                listaDobleInstruccionesDrones = lista_de_columna.Columna()
                nombre = listaDronesdelSistema.Pop().ObtenerNombre()
                for l in range(var1):
                    nombreAltura = listaAlturasValores.Pop().ObtenerNombre()
                    listaDobleInstruccionesDrones.Insertar(nombreAltura)
                    l += 1
                        
                InstruccionesDronesNombre = datoInstruccionesDronesNombre.datoInstruccionesDronesNombre(nombre, listaDobleInstruccionesDrones)
                listaInstruccionesDronesNombre.Insertar(InstruccionesDronesNombre)
                
                k += 1
            i += 1
            SistemaDrones = datoSistemasDrones.datoSistemasDrones(nombreSistema, var1, var2, listaInstruccionesDronesNombre)
            listaSistemasD.Insertar(SistemaDrones)
        listaSistemasD.ImprimirSistemas()

        for m in range(contadorMensajesNombres):
            var3 = listaMensajesNombres.Pop().ObtenerNombre()
            var4 = listaMensajesSistemaDrones.Pop().ObtenerNombre()
            var5 = int(listaCantInstrucciones.Pop().ObtenerNombre())
            listaDronesAlturas = listaMensajes.ListaMensajes()
            for n in range(var5):
                name = str(listaMensajesInstrucciones.Pop().ObtenerNombre()) 
                alt = str(listaMensajesInstrucciones2.Pop().ObtenerNombre())
                mensaje = datoMensaje.mensaje(name, alt)
                listaDronesAlturas.Insertar(mensaje)
                n += 1
            print(var3)
            print(var4)
            listaDronesAlturas.Imprimir()
            mensajes = datoInstrucciones.instrucciones(var3, var4, listaDronesAlturas)
            listaInst.Insertar(mensajes)
            m += 1
        #listaInst.ImprimirMensajes()

    def generarArchivo(self):
        pass
        
    
    def update_line_numbers(self, event=None):
        line_count = self.text_widget.get('1.0', tk.END).count('\n')
        if line_count != self.current_line:
            self.line_number_bar.config(state=tk.NORMAL)
            self.line_number_bar.delete(1.0, tk.END)
            for line in range(1, line_count + 1):
                self.line_number_bar.insert(tk.END, f"{line}\n")
            self.line_number_bar.config(state=tk.DISABLED)
            self.current_line = line_count
            
    def listaDrones(self):
        global listaDrones
        if listaDrones != None:
            if listaDrones.obtenerElementos != "Lista Vacía":
                listaDrones.ordenarLista()
                resultado = listaDrones.obtenerElementos()
                print(resultado)
                messagebox.showinfo("Lista de drones", str(resultado))
            else:        
                messagebox.showinfo("Error", "No se ha ingresado ningún dron")
        else:        
            messagebox.showinfo("Error", "No se ha ingresado ningún dron")
    
    def agregarDron(self):
        global listaDrones
        global contadorDrones
        nueva_ventana = Toplevel()
        nueva_ventana.geometry("350x100")
        nueva_ventana.title("Agregar Dron")

        label_texto = tk.Label(nueva_ventana, text="Ingrese el nombre del Dron:")
        label_texto.pack()
        entrada = tk.Entry(nueva_ventana)
        entrada.pack()

        def obtenertexto():
            dronIngresado=entrada.get()
            verificador = listaDrones.buscarElmentos(dronIngresado)
            if verificador == True:
                
                print(dronIngresado)
                Dron = datoDron.datoDron(dronIngresado, contadorDrones)
                listaDrones.Insertar(Dron)
                nueva_ventana.destroy()
            else:        
                messagebox.showinfo("Error", "Este dron ya existe!")

        boton_enviar=tk.Button(nueva_ventana, text="AGREGAR", command= obtenertexto)
        boton_enviar.pack()
    
    def sistemaDrones(self): 
        archivo = ET.parse(file_path)
        raiz = archivo.getroot()
        listaSistemaDronesNombreClon = listaSimple.ListaSimple()
        contadorSistemaDronesNombreClon = 0
        listaAlturasMaximasClon = listaSimple.ListaSimple()
        contadorAlturasMaximasClon = 0
        listaCantidadDronesClon = listaSimple.ListaSimple()
        contadorCantidadDronesClon = 0
        listaDronesdelSistemaClon = listaSimple.ListaSimple()
        contadorDronesdelSistemaClon = 0
        listaAlturasValoresClon = listaSimple.ListaSimple()
        contadorAlturasValoresClon = 0
        r = open("sistemaDrones.dot", "w", encoding="utf-8")
        r.write('''digraph G {
	node [shape=circle]
	nodo0 [label = "sistemas de drones"]
	nodo0[fontcolor = black]''')
        
        for elementos in raiz:
            for sistemaDrones in elementos.findall("sistemaDrones"):
                contadorSistemaDronesNombreClon += 1
                nombreSistema = str(sistemaDrones.get("nombre"))
                SistemaDronesNombre = datoSistemaDronesNombre.datoSistemaDronesNombre(nombreSistema, contadorSistemaDronesNombreClon)
                listaSistemaDronesNombreClon.Insertar(SistemaDronesNombre)
                for alturaMaxima in sistemaDrones.findall("alturaMaxima"):
                    contadorAlturasMaximasClon += 1
                    altura = str(alturaMaxima.text)
                    AlturasMaximas = datoAlturasMaximas.datoAlturasMaximas(altura, contadorAlturasMaximasClon)
                    listaAlturasMaximasClon.Insertar(AlturasMaximas)
                for cantidadDrones in sistemaDrones.findall("cantidadDrones"):
                    contadorCantidadDronesClon += 1
                    cantidad = str(cantidadDrones.text)
                    CantidadDrones = datoCantidadDrones.datoCantidadDrones(cantidad, contadorCantidadDronesClon)
                    listaCantidadDronesClon.Insertar(CantidadDrones)
                for contenido in sistemaDrones.findall("contenido"):
                    for dronesSistema in contenido.findall("dron"):
                        contadorDronesdelSistemaClon += 1
                        nombreDrones = str(dronesSistema.text)
                        DronesdelSistema = datoDronesdelSistema.datoDronesdelSistema(nombreDrones, contadorDronesdelSistemaClon )
                        listaDronesdelSistemaClon.Insertar(DronesdelSistema)
                    for alturas in contenido.findall("alturas"):
                        for alturaSistema in alturas.findall("altura"):
                            contadorAlturasValoresClon += 1
                            valor = str(alturaSistema.get("valor"))
                            alturaValor = str(alturaSistema.text)
                            AlturasValores = datoAlturasValores.datoAlturasValores(valor, alturaValor, contadorAlturasValoresClon)
                            listaAlturasValoresClon.Insertar(AlturasValores)

        for i in range(contadorSistemaDronesNombreClon):
            var1 = int(listaAlturasMaximasClon.Pop().ObtenerNombre())
            var2 = int(listaCantidadDronesClon.Pop().ObtenerNombre())
            nombreSistema = listaSistemaDronesNombreClon.Pop().ObtenerNombre()
            print("nombre: " + nombreSistema + " Altura Maxima " + str(var1) + " cantidad de drones " + str(var2))
            for k in range(var2):    
                nombre = listaDronesdelSistemaClon.Pop().ObtenerNombre()
                print("nombre " + nombre)
                for l in range(var1):
                    nombreAltura = listaAlturasValoresClon.Pop().ObtenerNombre()
                    print("nombre altura: " + nombreAltura)
                    l += 1
                k += 1
            i += 1
        
        r.write('''
}''')
        r.close()
        os.system("cmd /c dot -Tsvg sistemaDrones.dot > sistemaDrones.svg")
        
    def inicializar(self):
        global listaSistemasD
        global listaInst
        global listaDrones
        listaSistemasD.InicializarSistema()
        listaInst.InicializarSistema()
        listaDrones.InicializarSistema()
        messagebox.showinfo("Inicializar", "Se ha inicializado el sistema!")
    
    def ayuda(self):
        messagebox.showinfo("Información", "Néstor Enrique Villatoro Avendaño\n202200252\nIntroducción a la Programación y Computacion 2 Sección C\nIngenieria en Ciencias y Sistemas\n4to Semestre")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()