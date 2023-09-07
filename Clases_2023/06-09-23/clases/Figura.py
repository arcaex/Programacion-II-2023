class FiguraGeometricaClase:
    def __init__(self,cantidad_lados):
        self.cantidad_lados = cantidad_lados
        self.lados = []

    def calcular_perimetro(self):
        perimetro = 0
        for lado in self.lados:
            perimetro = perimetro + lado
        return perimetro
    
    def cargar_figura(self):
        for i in range(0,self.cantidad_lados):
            lado = int(input(f"Ingrese el lado {i+1} \n"))
            self.lados.append(lado)
