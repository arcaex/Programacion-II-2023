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
    def __init__(self,nombre,apellido,edad,peso,año_ingreso,matricula,carrera):
        super().__init__(nombre,apellido,edad,peso)
        self.matricula = matricula
        self.carrera = carrera
        self.año_ingreso = año_ingreso
    
    def calcular_antiguedad(self,año_actual):
        antiguedad = año_actual - self.año_ingreso
        return antiguedad
    
persona2 = Alumno("Maria","Guzman",26,67,2021,7789,"Tec. en Programación")
persona2.mostrar_datos()
print(persona2.calcular_antiguedad(2023))

class AlumnoPrimaria(Alumno):
    def __init__(self,nombre,apellido,edad,peso,año_ingreso,tutor,curso):
        super().__init__(nombre,apellido,edad,peso,año_ingreso,matricula=0,carrera='')
        self.curso = curso
        self.tutor = tutor
    
    def mostrar_tutor(self):
        self.tutor.mostrar_datos()


primaria1 = AlumnoPrimaria("Pedro","Perez",4,20,2023,persona1,"Salita Celeste")
primaria1.mostrar_tutor()
print(primaria1.calcular_antiguedad(2023))
primaria1.mostrar_datos()


