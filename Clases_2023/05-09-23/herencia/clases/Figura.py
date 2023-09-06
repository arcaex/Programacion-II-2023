class FiguraGeometrica:
    def __init__(self,cantidad_lados):
        self.lados = []
        self.cantidad_lados = cantidad_lados
    
    def ingresar_lados(self):
        for i in range(0,self.cantidad_lados):
            lado = int(input(f"Ingresar el lado {i+1} \n"))
            self.lados.append(lado)

    def calcular_perimetro(self):
        perimetro = 0
        for lado in self.lados:
            perimetro = perimetro + lado
        return perimetro