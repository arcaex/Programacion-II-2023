class Circunferencia:
    def __init__(self,radio):
        self.radio = radio
    def area(self):
        resultado = 3.14 * self.radio**2
        return resultado
    def perimetro(self):
        resultado = 2*3.14*self.radio
        return resultado
    
circulo1 = Circunferencia(5)
print(circulo1.radio)
print(circulo1.area())
print(circulo1.perimetro())


