class instrucciones:
    
    def __init__(self,nombreInstruccion, sistema, instrucciones):
        self.nombre_intruccion=nombreInstruccion
        self.sistema_usar=sistema
        self.instrucciones=instrucciones

    def ObtenerNombre(self):
        return self.nombre_intruccion
    
    def ObtenerSistema_a_Usar(self):
        return self.sistema_usar