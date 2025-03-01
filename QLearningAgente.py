import random
import numpy as np

class QLearningAgente:
    def __init__(self, state_size, action_size, alpha=0.1, gamma=0.6, epsilon=0.1):
        self.state_size = state_size
        self.action_size = action_size
        self.alpha = alpha  # Tasa de aprendizaje
        self.gamma = gamma  # Factor de descuento
        self.epsilon = epsilon  # Probabilidad de exploración
        self.q_table = np.zeros((state_size, action_size))  # Tabla Q inicializada en ceros

    def elegirAccion(self, state_index):
        # Verificar que el índice esté dentro de los límites
        if state_index < 0 or state_index >= self.state_size:
            return random.randint(0, self.action_size - 1)  # Explorar como fallback
        
        if self.action_size == 1:
            return 0  # Si solo hay una acción posible, siempre elige esa

        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_size - 1)  # Explorar
        else:
            return np.argmax(self.q_table[state_index])  # Explotar

    def actualizarQ(self, state, action, reward, next_state):
        # Convertir los estados en índices válidos
        state_index = self.state_to_index(state)
        next_state_index = self.state_to_index(next_state)
        
        # Asegurarse de que los índices estén dentro de los límites
        state_index = min(max(state_index, 0), self.state_size - 1)
        next_state_index = min(max(next_state_index, 0), self.state_size - 1)

        best_next_action = np.argmax(self.q_table[next_state_index])
        td_target = reward + self.gamma * self.q_table[next_state_index][best_next_action]
        td_error = td_target - self.q_table[state_index][action]
        self.q_table[state_index][action] += self.alpha * td_error

    def state_to_index(self, state):
        # Convertir el estado en un índice entero
        state = state.astype(int)
        state_str = ''.join(map(str, state))
        state_index = int(state_str) % self.state_size  # Asegurarse de que el índice esté dentro de los límites
        return state_index

