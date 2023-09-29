import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import xml.etree.ElementTree as ET
import doble.listaDoble as listaDoble
import simple.listaSimple as listaSimple
import objetos.datoDron as datoDron
import objetos.datoSistemaDronesNombre as datoSistemaDronesNombre
import objetos.datoAlturasMaximas as datoAlturasMaximas
import objetos.datoCantidadDrones as datoCantidadDrones
import objetos.datoDronesdelSistema as datoDronesdelSistema
import objetos.datoInstruccionesDrones as datoInstruccionesDrones
import objetos.datoInstruccionesDronesNombre as datoInstruccionesDronesNombre
import objetos.datoAlturasValores as datoAlturasValores
from tkinter import filedialog, messagebox
from tkinter import ttk
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

global listaDobleInstruccionesDrones 
listaDobleInstruccionesDrones = None

global listaInstruccionesDronesNombre
listaInstruccionesDronesNombre = None

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
                        print("dron del sistema: " + nombreDrones)
                    for alturas in contenido.findall("alturas"):
                        for alturaSistema in alturas.findall("altura"):
                            contadorAlturasValores += 1
                            valor = str(alturaSistema.get("valor"))
                            alturaValor = str(alturaSistema.text)
                            AlturasValores = datoAlturasValores.datoAlturasValores(valor, alturaValor, contadorAlturasValores)
                            listaAlturasValores.Insertar(AlturasValores)
            for Mensaje in  elementos.findall("Mensaje"):
                nombreMensaje = str(Mensaje.get("nombre"))
                print("el nombre del mensaje es: " + nombreMensaje)
                for sistemadeDrones in  Mensaje.findall("sistemaDrones"):
                    sistema = str(sistemadeDrones .text)
                    print("el sistema de drones que se utiliza es: " + sistema)
                for instrucciones in  Mensaje.findall("instrucciones"):
                    for instruccion in instrucciones.findall("instruccion"):
                        dron = str(instruccion.get("dron"))
                        alturaDron = str(instruccion.text)
                        print("El dron " + dron + " se mueve a la altura " + alturaDron)
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

    def generarArchivo(self):
        global listaSistemaDronesNombre
        global contadorSistemaDronesNombre
        global listaAturasMaximasl
        global contadorAlturasMaximas
        global listaCantidadDrones
        global contadorCantidadDrones
        global listaDronesdelSistema
        global contadorDronesdelSistema
        global listaAlturasValores
        global contadorAlturasValores
        global listaDobleInstruccionesDrones
        global listaInstruccionesDronesNombre

        for i in range(contadorAlturasMaximas):
            var1 = int(listaAlturasMaximas.Pop().ObtenerNombre())
            for j in range(contadorCantidadDrones):
                var2 = int(listaCantidadDrones.Pop().ObtenerNombre())
                for k in range(var2):
                    listaInstruccionesDronesNombre = listaSimple.ListaSimple()
                    listaDobleInstruccionesDrones = listaDoble.ListaDoble()
                    contador = 1
                    for l in range(var1):
                        nombreAltura = listaAlturasValores.Pop().ObtenerNombre()
                        InstruccionesDrones = datoInstruccionesDrones.datoInstruccionesDrones(contador, nombreAltura)
                        listaDobleInstruccionesDrones.Insertar(InstruccionesDrones)
                        contador +=1
                        l += 1
                    nombre = listaDronesdelSistema.Pop().ObtenerNombre()
                    InstruccionesDronesNombre = datoInstruccionesDronesNombre.datoInstruccionesDronesNombre(listaDobleInstruccionesDrones, nombre)
                    listaInstruccionesDronesNombre.Insertar(InstruccionesDronesNombre)
                    k += 1
                j += 1
            i += 1
        print(listaInstruccionesDronesNombre.Pop().ObtenerIndice())
        
    
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
        dron = "DronX"
        verificador = listaDrones.buscarElmentos(dron)
        if verificador == True:
            contadorDrones += 1
            Dron = datoDron.datoDron(dron, contadorDrones)
            listaDrones.Insertar(Dron)
            messagebox.showinfo("Dron añadido!", "Se añadió el dron exitosamente!")
        else:        
            messagebox.showinfo("Error", "Este dron ya existe!")
    
    def sistemaDrones(self):
        a=1
        
    def inicializar(self):
        a=1
 


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()