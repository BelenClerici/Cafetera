class Cafetera:
    def __init__(self):
        self.cap_max= 1000
        self.cant_actual =0
    
    def llenar_cafetera(self):
        self.cap_max= self.cant_actual

    def agregar_cafe(self,cantidad):
        if self.can_actual + cantidad > self.cap_max:
            raise ValueError (" La cantidad total supera la capacidad máxima" )
            self.cant_actual = self.cant_actual + cantidad 
        else:
            self.cant_actual = 0 
    
    def vaciar_cafetera():
        self.cant_actual=0
        