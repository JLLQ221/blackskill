import gym 
from gym import spaces
import numpy as np
from QLearningAgente import QLearningAgente

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
        
        # Inicializar Q-Learning Agent
        state_size = 10**5  # Ejemplo, ajusta según tus necesidades
        action_size = self.action_space.n
        self.q_agent = QLearningAgente(state_size=state_size, action_size=action_size)

    def reset(self):
        # Resetear el entorno a un estado inicial
        self.state = np.zeros(5)  # Define un estado inicial apropiado
        return self.state

    def step(self, action):
     reward = 0
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
     state = self.state
     state_index = self.state_to_index(state)
     habilidad_index = self.q_agent.elegirAccion(state_index)
     return habilidad_index

    def elegirMejorHabilidad(self):
        # Obtener el estado actual del juego
        state = self.state
        # Convertir el estado en un índice válido
        state_index = self.state_to_index(state)
        # Elegir la mejor acción usando Q-Learning
        habilidad_index = self.q_agent.elegirAccion(state_index)
        return habilidad_index

    def state_to_index(self, state):
        # Convertir el estado en un índice entero
        state = state.astype(int)
        state_str = ''.join(map(str, state))
        state_index = int(state_str) % self.q_agent.state_size  # Asegurarse de que el índice esté dentro de los límites
        return state_index

    def continuar(self):
        # Continuar la lógica aquí después de la espera
        pass

    def get_updated_state(self):
     nuevo_estado = np.array([
        self.context.getCountVidas(),
        self.juego.jugadores[0].getCountVidas(),
        len(self.context.getHabilidades()),
        len(self.context.getCards()),
        len(self.juego.jugadores[0].getCards()),
        self.context.getCountHabilidades()  # Número de habilidades disponibles
    ], dtype=np.float32)
     return nuevo_estado


    def check_done(self):
     # Verifica si la vida de alguno de los jugadores ha llegado a cero
     if self.juego.jugadores[0].getCountVidas() <= 0 or self.context.getCountVidas() <= 0:
        return True
     # Verifica si el turno del jugador ha terminado
     if self.context.turno == False:
        return True
     if len(self.juego.cartas) <= 0:
        return True
     return False


    def render(self, mode='human'):
        # Renderizar el entorno (opcional)
        pass

