import random
import gym
from ia import ia  # Asegúrate de importar el entorno creado

# Crear el entorno
env = ia()

# Definir parámetros de entrenamiento
episodes = 100  # Número de episodios

for episode in range(episodes):  # Utilizar range para iterar
    state = env.reset()
    done = False

    while not done:
        action = env.action_space.sample()  # Tomar una acción aleatoria (puedes mejorar esto)
        state, reward, done, info = env.step(action)
        
        if done:
            break

    print(f'Episodio {episode} terminado')

env.close()
