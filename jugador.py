from tkinter import Label
class jugador:

    def __init__(self, countLabel, nombre, ventana , y,  lifeLabel = None, ):
        self.vidas = 3
        self.cartas = []
        self.habilidades = []
        self.ventana = ventana
        self.countMaso = 0
        self.turno = False
        self.countLabel = countLabel
        self.lifeLabel = lifeLabel
        self.nombre = nombre
        self.masoPerdido = False
        self.xStartLBCards = 0.4
        self.y = y
        
    def insertCard (self ,carta):
        self.cartas.append(carta)
        self.habilidades.append(carta.habilidad)
        if(self.getCountHabilidades() > 3):
          self.habilidades.pop(0)
        self.countMaso += carta.valor
        self.countLabel.config(text=str(self.countMaso))
        if(self.getCountMaso() > 21):
          self.turno = False
          self.masoPerdido = True

    def vaciarMaso(self):
       self.cartas=[]
       self.countMaso = 0
       self.habilidades = []
       self.updateLabels()
       self.masoPerdido = False
       self.turno = False  

    def colocarCardsLabels(self):
       xExponencial = self.xStartLBCards
       for carta in self.cartas:
         newCard = Label(self.ventana ,background="white", text=carta.valor, relief="solid")
         newCard.place(relx=xExponencial, rely=self.y, relwidth=0.06, relheight=0.12)
         xExponencial += 0.04

    def getCards (self):
       return self.cartas.copy()

    def popHabilidad(self, i):
     if 0 <= i < len(self.habilidades):
        habilidadTemporal = self.habilidades[i]
        self.habilidades.pop(i)
        return habilidadTemporal
     
    def getHabilidades(self):
       self.stateHabilidad = True
       return self.habilidades.copy()
    
    def getCountHabilidades (self):
       return len(self.habilidades)

    def popVida(self):
       self.vidas -= 1
       self.lifeLabel.config(text=self.nombre + " vidas: " + str(self.vidas))
   
    def putVida(self):
       self.vidas += 1
       self.lifeLabel.config(text=self.nombre + " vidas: " + str(self.vidas))
    
    def getCountVidas(self):
       return self.vidas
    
    def getCountMaso(self):
       return self.countMaso
    
    def plantarse(self):
       self.turno = False
   
    def updateLabels(self):
      self.countLabel.config(text=str(self.countMaso))

    def setLabels (self, labelCount, labelCartas = None):
       self.countLabel = labelCount
       self.cartasLabel = labelCartas  