class HeuristicAgent:
    def __init__(self):
        pass
    
    def elegir_accion(self, state):
        # Definir la heurística aquí
        if state[0] < 2:  # Si tienes menos de 2 vidas, plantarse
            return 2
        elif state[2] > 0:  # Si tienes habilidades disponibles, usarlas
            return 0
        else:  # De lo contrario, tomar una carta
            return 1
