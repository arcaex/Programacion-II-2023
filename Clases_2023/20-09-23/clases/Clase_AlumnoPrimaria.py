from Clase_Alumno import Alumno

class AlumnoPrimaria(Alumno):
    def __init__(self,nombre,apellido,edad,peso,año_ingreso,tutor,curso):
        super().__init__(nombre,apellido,edad,peso,año_ingreso,matricula=0,carrera='')
        self.curso = curso
        self.tutor = tutor
    
    def mostrar_tutor(self):
        self.tutor.mostrar_datos()