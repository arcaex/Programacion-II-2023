class Persona:
    def __init__(self,nombre,apellido,edad,peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso

    def mostrar_datos(self):
        print(f"{self.nombre},{self.apellido} {self.edad} años - {self.peso} Kg")