from clases.Figura import FiguraGeometricaClase

class TrianguloClase(FiguraGeometricaClase):
    def __init__(self):
        super().__init__(3)
    
    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        s2 = 1
        for lado in self.lados:
            s2 = s2 * (s-lado)
        area = (s*s2) ** 0,5
        return area
    
    def tipo_triangulo(self):
        if self.lados[0] == self.lados[1] and self.lados[2] == self.lados[0]:
            print("Equilatero")
        elif self.lados[0] != self.lados[1] and self.lados[2] != self.lados[0]:
            print("Escaleno")
        else:
            print("Isosceles")

    