from Clase_Persona import Persona

class Alumno(Persona):
    def __init__(self,nombre,apellido,edad,peso,año_ingreso,matricula,carrera):
        super().__init__(nombre,apellido,edad,peso)
        self.matricula = matricula
        self.carrera = carrera
        self.año_ingreso = año_ingreso
            
    def calcular_antiguedad(self,año_actual):
        antiguedad = año_actual - self.año_ingreso
        return antiguedad
