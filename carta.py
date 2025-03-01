class carta:

    def __init__(self, valor, tipo):
        self.valor = valor
        self.habilidad = ""
        self.tipo = tipo
        self.definirHabilidad()
    
    # Colocar las distintas habilidades dependiendo de la carta
    def definirHabilidad(self):
        match (self.tipo):
            case "As":
                self.habilidad= "Vida"
            case "Figura":
                self.habilidad="Sg. carta"
            case "Rombo":
                self.habilidad="Quitar vida"  
            case _:
                self.habilidad= ""
     