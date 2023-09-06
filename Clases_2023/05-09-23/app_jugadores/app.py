from clases.Jugadores import Jugador, Equipo

menu = '''### MENÚ ###
- 1 Agregar Jugador
- 2 Mostrar Jugadores
- 3 Ver Antigüedad
- 4 Ver Plazas Disponibles
- 5 Salir'''

opc = "0"

equipo_nuevo = Equipo(11)

while opc != "5":
    print(menu)
    opc = input("Ingrese Opcion \n")
    if opc == "1":
        nombre = input("Ingrese Nombre \n")
        apellido = input("Ingrese Apellido \n")
        numero = input("Ingrese Número \n")
        año_ingreso = int(input("Ingrese Año \n"))
        jugador_ingresado = Jugador(nombre,apellido,numero,año_ingreso)
        equipo_nuevo.agregar_jugador(jugador_ingresado)
    elif opc == "2":
        equipo_nuevo.mostrar_jugadores()
    elif opc == "3":
        equipo_nuevo.jugador_nuevo()
    else:
        print(f"Las plazas disponibles son: {equipo_nuevo.plazas_disponibles()}")