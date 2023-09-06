class Jugador:
    def __init__(self, nombre, apellido, numero, año_ingreso):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.año_ingreso = año_ingreso


class Equipo:
    def __init__(self,cantidad_maxima):
        self.lista_jugadores = []
        self.cantidad_maxima = cantidad_maxima

    def agregar_jugador(self,jugador):
        self.lista_jugadores.append(jugador)

    def mostrar_jugadores(self):
        for jugador in self.lista_jugadores:
            self.mostrar_jugador(jugador)

    def mostrar_jugador(self,jugador):
        print(f"{jugador.nombre}, {jugador.apellido} - {jugador.numero} ({jugador.año_ingreso})")
        
    def jugador_nuevo(self):
        
        jugador_viejo = self.lista_jugadores[0]
        jugador_nuevo = self.lista_jugadores[0]
        
        for jugador in self.lista_jugadores:
            if jugador_viejo.año_ingreso > jugador.año_ingreso:
                jugador_viejo = jugador
            if jugador_nuevo.año_ingreso < jugador.año_ingreso:
                jugador_nuevo = jugador
        
        print(f"El jugador más viejo es \n")
        print(self.mostrar_jugador(jugador_viejo))

        print(f"El jugador más nuevo es \n")
        print(self.mostrar_jugador(jugador_nuevo))
    
    def plazas_disponibles(self):
        return self.cantidad_maxima - len(self.lista_jugadores)