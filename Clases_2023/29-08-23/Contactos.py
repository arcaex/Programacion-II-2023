class Contacto:
    def __init__(self,nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

class Agenda:
    def __init__(self):
        self.listadoContactos = []

    def agregarContacto(self,contacto):
        self.listadoContactos.append(contacto)

    def mostrarContactos(self):
        for elemento in self.listadoContactos:
            print(elemento.nombre,",",elemento.apellido, " telefono: ", elemento.telefono)

agenda1 = Agenda()

opc = "0"
while opc!="3":
    opc = input("1. Agregar Contacto \n 2. Mostrar Listado \n 3.Salir \n")
    if opc == "1":
        nombre = input("Ingrese Nombre \n")
        apellido = input("Ingrese Apellido \n")
        telefono = int(input("Ingrese Telefono \n"))
        contacto1 = Contacto(nombre,apellido,telefono)
        agenda1.agregarContacto(contacto1)

    if opc == "2":
        agenda1.mostrarContactos()


