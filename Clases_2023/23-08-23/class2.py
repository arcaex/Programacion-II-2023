# class Persona:
    
#     # Atributos 
#     def __init__(self,nombre,apellido,año_nacimiento):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.año_nacimiento = año_nacimiento
#         self.habilitado = False
    
#     # Metodos
#     def calcular_edad(self):
#         edad = 2023 - self.año_nacimiento
#         return edad

# alumno = Persona("Pedro","Perez",1990)
# print(alumno.nombre)
# print(alumno.calcular_edad())


class PersonalUTN:
    def __init__(self,dni,nombre,fecha_nacimiento,fecha_ingreso,sueldo):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.sueldo = sueldo
    
    def calcular_antiguedad(self):
        antiguedad = 2023 - self.fecha_ingreso
        return antiguedad
    
    def calcular_vacaciones(self):
        antiguedad = self.calcular_antiguedad()
        # Hasta 5 años - 15 días
        # De 5 a 10 Años - 21 días
        # De 10+ Años - 30 días
        if antiguedad < 5 :
            return 15
        elif antiguedad < 10:
            return 21
        else:
            return 30
        
    def calcular_aguinaldo(self):
        aguinaldo = self.sueldo/2
        return aguinaldo
    
    def mostrar_situacion(self):
        if self.sueldo < 170000:
            print("Baja")
        elif self.sueldo < 200000:
            print("Media")
        else:
            print("Alta")

noDocente = PersonalUTN(33000333,"Jorge",1988,2015,150000)
print(noDocente.calcular_antiguedad())
print(noDocente.calcular_vacaciones())
print(noDocente.calcular_aguinaldo())
print(noDocente.mostrar_situacion())