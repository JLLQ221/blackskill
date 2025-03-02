Para poder instalar el proyecto debemos de:

1.-Primero debemos de abrir el proyecto en Visual Studio y descargar la extensión de Python luego de ello debemos de instalar el compilador de Python (se encuentra en la Windows Store para más seguridad).

2.-Luego de tener el proyecto abierto en Visual o en la terminal instalaremos PIL (Pillow) para el manego de imagenes con el comando pip install pillow.

3.-También debemos de instalar la libreria GYM de python con el comando pip install gym

La clase HeuristicAgent utiliza una heurística para tomar decisiones basadas en el estado actual. Una heurística es una regla o un conjunto de reglas que permiten encontrar soluciones rápidas y satisfactorias para problemas complejos. A continuación, te explico cómo funciona la heurística en este ejemplo:

Si el primer elemento del estado (state[0]) es menor que 2: Esto indica que el agente tiene menos de 2 vidas. La heurística en este caso es plantarse (retornar 2).

Si el tercer elemento del estado (state[2]) es mayor que 0: Esto indica que el agente tiene habilidades disponibles. La heurística en este caso es usar esas habilidades (retornar 0).

En cualquier otro caso: Si ninguna de las condiciones anteriores se cumple, la heurística es tomar una carta (retornar 1).

Las heurísticas ayudan a simplificar la toma de decisiones en situaciones donde un análisis completo sería demasiado costoso o complicado. Este enfoque puede no ser óptimo en todos los casos, pero ofrece una manera eficiente de actuar en la mayoría de las situaciones.

