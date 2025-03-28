import gym 
from gym import spaces
import numpy as np
from HeuristicAgent import HeuristicAgent

class ia(gym.Env):
    def __init__(self, juego):
        super(ia, self).__init__()
        # Definir las acciones y el espacio de observación
        self.action_space = spaces.Discrete(3)  # Ejemplo: 0 = Habilidad, 1 = Pedir carta, 2 = Plantarse
        self.observation_space = spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)
        self.state = self.reset()
        self.juego = juego
        self.context = juego.jugadorIA
        self.history = []
        
        # Inicializar agente heurístico
        self.h_agent = HeuristicAgent()

    def reset(self):
        # Resetear el entorno a un estado inicial
        self.state = np.zeros(5)  # Define un estado inicial apropiado
        return self.state

    def step(self, action=None):
        done = self.check_done()
        reward = 0
        if action is None:
            action = self.h_agent.elegir_accion(self.state)

        if action == 0:  # Usar habilidad
            if self.context.getCountHabilidades() > 0:
                habilidad_index = self.elegirMejorHabilidad()
                reward = self.juego.usarHabilidadIA(habilidad_index)
            else:
                reward = -5  # Penalización por intentar usar una habilidad sin tener ninguna
        elif action == 1:  # Pedir carta
            reward = self.juego.tomarCartaIA()
        elif action == 2:  # Plantarse
            reward = self.juego.plantarseIA()

        self.state = self.get_updated_state()
        done = self.check_done()

        info = {
            "action_id": action,
            "previous_actions": self.history,
        }

        return self.state, reward, done, info

    def elegirMejorHabilidad(self):
        # Implementa una lógica adecuada para elegir la mejor habilidad sin usar q_agent
        # Por ahora, elegiremos la primera habilidad disponible como ejemplo
        if len(self.context.getHabilidades()) > 0:
            return 0  # Índice de la primera habilidad disponible
        return -1  # No hay habilidades disponibles

    def state_to_index(self, state):
        # No necesitamos este método para el agente heurístico, así que puedes omitirlo
        pass

    def continuar(self):
        # Continuar la lógica aquí después de la espera
        pass

    def get_updated_state(self):
        nuevo_estado = np.array([
            self.context.getCountVidas(),
            self.juego.jugador1.getCountVidas(),
            len(self.context.getHabilidades()),
            len(self.context.getCards()),
            len(self.juego.jugadores[0].getCards()),
            self.context.getCountHabilidades()  # Número de habilidades disponibles
        ], dtype=np.float32)
        return nuevo_estado

    def check_done(self):
        # Verifica si la vida de alguno de los jugadores ha llegado a cero
        if self.juego.jugador1.getCountVidas() <= 0 or self.context.getCountVidas() <= 0:
            return True
        # Verifica si el turno del jugador ha terminado
        if not self.context.turno:
            return True
        if len(self.juego.cartas) <= 0:
            return True
        return False

    def render(self, mode='human'):
        # Renderizar el entorno (opcional)
        pass
