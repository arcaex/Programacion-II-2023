from Figura import FiguraGeometrica

class FiguraTriangulo(FiguraGeometrica):
    def __init__(self,altura):
        super().__init__(3)
        self.altura = altura
    
    def calcular_area(self):
        return (self.lados[2] * self.altura)/2
