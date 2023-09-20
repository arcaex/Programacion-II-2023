class Persona:
    def __init__(self,nombre,apellido,edad,peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso

    def mostrar_datos(self):
        print(f"{self.nombre},{self.apellido} {self.edad} años - {self.peso} Kg")


persona1 = Persona("Jorge","Lopez",23,86)
persona1.mostrar_datos()

class Alumno(Persona):
    def __init__(self,nombre,apellido,edad,peso,matricula,carrera,año_ingreso):
        super().__init__(nombre,apellido,edad,peso)
        self.matricula = matricula
        self.carrera = carrera
        self.año_ingreso = año_ingreso
    
    def calcular_antiguedad(self,año_actual):
        antiguedad = año_actual - self.año_ingreso
        return antiguedad
    

persona2 = Alumno("Maria","Guzman",26,67,7789,"Tec. en Programación",2021)
persona2.mostrar_datos()
print(persona2.calcular_antiguedad(2023))

