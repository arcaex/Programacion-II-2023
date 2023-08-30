class Usuario:
    def __init__(self,nombre,apellido,mail,clave):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.clave = clave
    def mostrar_datos(self):
        return f"nombre:{self.nombre} apellido:{self.apellido} clave:{self.clave} mail:{ self.mail}"
    def cambiar_clave(self,clave_nueva):
        self.clave = clave_nueva
    def cambiar_nombre(self,nombre_nuevo):
        self.nombre = nombre_nuevo
    def confirmar_mail(self,mail):
        if self.mail == mail:
            print("Correo Verificado")
        else:
            print("Correo No Verificado")

class Agenda:
    def __init__(self):
        self.Lista_Usuarios = []

    def cargar_usuario(self):
        nombre = input("Ingresar el Nombre \n")
        apellido = input("Ingresar Apellido \n")
        mail = input("Ingrese Mail \n")
        clave = input("Ingrese Clave \n")
        usuario1 = Usuario(nombre,apellido,mail,clave)
        self.Lista_Usuarios.append(usuario1)
    
    def mostrar_usuario(self,indice):
        print(self.Lista_Usuarios[indice].mostrar_datos())

    def mostrar_todos(self):
        for usuario in self.Lista_Usuarios:
            print(usuario.mostrar_datos())

agenda = Agenda()
opc = "0"
while opc!="4":
    print("1. Cargar Usuario \n")
    print("2. Mostrar Todos los Usuarios \n")
    print("3. Mostrar un Usuario \n")
    print("4. Salir \n")
    opc = input("Ingrese una Opcion \n")
    if opc == "1" :
        agenda.cargar_usuario()
    elif opc == "2":
        agenda.mostrar_todos()
    elif opc == "3":
        indice = int(input("Ingrese Indice \n"))
        agenda.mostrar_usuario(indice)
    else:
        print("Nos vemos! Bye =D")

# usuario1 = Usuario("Juan","Lopez","jlopez@gmail.com","123")
# usuario2 = Usuario("Juana","Moreno","jmoreno@gmail.com","456")
# usuario3 = Usuario("Pepe","Pepin","ppepin@gmail.com","789")
# agenda.Lista_Usuarios.append(usuario1)
# agenda.Lista_Usuarios.append(usuario2)
# agenda.Lista_Usuarios.append(usuario3)