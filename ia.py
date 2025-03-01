class iaHeuristico:
    def __init__(self, juego):
        self.juego = juego
        self.context = juego.jugadorIA

    def decidir_accion(self):
        suma_cartas = self.suma_cartas(self.context.getCards())
        suma_cartas_oponente = self.suma_cartas(self.juego.jugadores[0].getCards())

        # Usar habilidad si la vida del jugador es baja o la vida del oponente es baja
        if self.context.getCountHabilidades() > 0 and (self.context.getCountVidas() < 3 or self.juego.jugadores[0].getCountVidas() < 3):
            return 0  # Usar habilidad

        # Tomar carta si la suma de cartas de la IA es menor o igual a 16
        if suma_cartas <= 16:
            return 1  # Pedir carta

        # Plantarse si la suma de cartas de la IA es 17 o más
        if suma_cartas >= 17:
            return 2  # Plantarse

        # Acción predeterminada
        return 1  # Pedir carta

    def realizar_accion(self, action):
        if action == 0:
            habilidad_index = self.elegirMejorHabilidad()
            self.juego.usarHabilidadIA(habilidad_index)
        elif action == 1:
            self.juego.tomarCartaIA()
        elif action == 2:
            self.juego.plantarseIA()

    def elegirMejorHabilidad(self):
        habilidades = self.context.getHabilidades()
        if len(habilidades) > 0:
            return 0  # Ejemplo: siempre usar la primera habilidad disponible
        return -1  # No hay habilidades disponibles

    def suma_cartas(self, cartas):
        # Calcular la suma de las cartas considerando el valor del As como 1 o 11
        suma = 0
        ases = 0
        for carta in cartas:
            valor = carta.getValor()  # Asumiendo que las cartas tienen un método getValor()
            if valor == 1:  # Es un As
                ases += 1
                valor = 11
            suma += valor

        # Ajustar el valor de los ases si la suma es mayor a 21
        while suma > 21 and ases > 0:
            suma -= 10
            ases -= 1

        return suma
