from clases.Figura import FiguraGeometricaClase

class RectanguloClase(FiguraGeometricaClase):
    def __init__(self):
        super().__init__(4)
    
    def calcular_area(self):
        base = self.lados[0]
        altura = self.lados[0]
        for lado in self.lados:
            if lado > base:
                base = lado
            if lado < altura:
                altura = lado
        
        return base*altura