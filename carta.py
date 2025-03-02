class carta:

    def __init__(self, valor, tipo):
        self.valor = valor
        self.habilidad = ""
        self.tipo = tipo
        self.definirHabilidad()
    
    # Colocar las distintas habilidades dependiendo de la carta
    def definirHabilidad(self):
        match (self.tipo):
            case "J":
                self.habilidad= "Vida"
            case "Q":
                self.habilidad="Sg. carta"
            case "K":
                self.habilidad="Quitar vida"  
            case _:
                self.habilidad= None
     