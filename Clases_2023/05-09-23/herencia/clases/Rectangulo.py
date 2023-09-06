from Figura import FiguraGeometrica

class FiguraRectangulo(FiguraGeometrica):
    def __init__(self):
        super().__init__(4)
    
    def calcular_area(self):
        return self.lados[0]*self.lados[1]