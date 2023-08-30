# class Persona:
#     # Atributos
#     def __init__(self,nombre,apellido,fecha_nacimiento):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.fecha_nacimiento = fecha_nacimiento
    
#     # Metodos
#     def calcular_edad(self):
#         edad = 2023 - self.fecha_nacimiento
#         return edad

# jorge = Persona("Jorge","Gracia",1988) # Instanciar un objeto

# print(jorge.apellido)
# print(jorge.calcular_edad())

# class Monitor():
#     # Atributos
#     def __init__(self,marca,resolucion,brillo,color):
#         self.marca = marca
#         self.resolucion = resolucion
#         self.brillo = brillo
#         self.color = color
#         self.encendido = False
    
#     # Metodos
#     def encender_monitor(self):
#         self.encendido = True
    
#     def cambiar_brillo(self,porcentaje):
#         self.brillo = porcentaje

# monitor_aula = Monitor("TCL","FullHD-4k", 100,"Gris")

# print(monitor_aula.encendido)
# monitor_aula.encender_monitor()
# print(monitor_aula.encendido)

# print(monitor_aula.brillo)
# monitor_aula.cambiar_brillo(50)
# print(monitor_aula.brillo)

# print(monitor_aula.marca)


class Operacion:
    def __init__(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        resultado = self.numero1 + self.numero2
        return resultado
    
    def restar(self):
        if self.numero1 > self.numero2:
            resultado = self.numero1 - self.numero2
        else:
            resultado = self.numero2 - self.numero1
        return resultado
     
op = Operacion(3,5)
print(op.sumar())
print(op.restar())
        
            


