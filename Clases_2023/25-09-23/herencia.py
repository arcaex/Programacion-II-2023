# padre -> hija 

# padre -> Atributos -> Variable (cualidad que tenga el objeto: color, tamaño,etc)
# -> metodos -> Funciones (Acciones)

# Persona -> Atributos -> Nombre, Apellido, Edad, Altura, Peso 
#            Método -> mostrar_datos()
#                   -> año_nacimiento()

class Persona:
    def __init__(self,nombre,apellido,edad,altura=None,peso=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.edad} años - {self.altura}m - {self.peso}kg"
    
    def año_nacimiento(self,año_actual):
        nacimiento = año_actual - self.edad
        return nacimiento
    
# Alumno -> Att -> Carrera, Matricula, Año_Ingreso, Comision, Notas
#           Met -> Calcular_Promedio, antiguedad_carrera, cargar_notas

class Alumno(Persona):
    def __init__(self,nombre,apellido,edad,carrera,matricula,año_ingreso,comision):
        super().__init__(nombre,apellido,edad,None,None)
        self.carrera = carrera
        self.matricula = matricula
        self.año_ingreso = año_ingreso
        self.comision = comision
        self.notas = []

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.edad} años - {self.carrera} {self.comision} {self.año_ingreso}"

    def calcular_promedio(self):
        sumatoria = sum(self.notas)
        # sumatoria = 0
        # for nota in self.notas:
        #     sumatoria += nota
        promedio = sumatoria / len(self.notas) 
        return promedio
    
    def antiguedad_carrera(self,año_actual):
        return año_actual - self.año_ingreso
    
    def cargar_notas(self,nota):
        self.notas.append(nota)

alumno1 = Alumno("Maria","Lopez",20,"TUP",1234,2022,"A")
print(alumno1)
print(alumno1.antiguedad_carrera(2023))
alumno1.cargar_notas(6)
alumno1.cargar_notas(8)
alumno1.cargar_notas(9)
print(alumno1.calcular_promedio())
print(alumno1.año_nacimiento(2023))


# Clase Hija de la Clase Persona que se llame AlumnoPrimaria
# Atributo : Tutor -> Objeto Persona
# Atributo : Notas
# Método : mostrar_datos_tutor()
# Método : año_egreso_primaria() -> 12 años
# Método : calcular_promedio()
