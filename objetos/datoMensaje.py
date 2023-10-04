class mensaje:
    def  __init__(self, dron, instruccion):
        self.dron=dron
        self.instruccion=instruccion
    
    def ObtenerDron(self):
        return self.dron
    
    def ObtenerInstruccion(self):
        return self.instruccion