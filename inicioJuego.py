from tkinter import Label, Button
from jugador import jugador
from carta import carta
from ia import ia

class inicioJuego:
    def __init__(self, ventana):
       self.colorUniversal = "#003d36"
       self.colorAccion = "#122962"
       self.colorBotons= "blue"
       self.activeForeground = "#d0d2d5"
       self.ventana = ventana
       self.colocarLabelImp()
       self.jugador1 = jugador(countLabel=self.labelCountJugador, lifeLabel=self.labelLifeJugador, y=0.8 , ventana=self.ventana ,  nombre="Tus")
       self.jugadorIA = jugador(countLabel=self.labelCountIaJugador, lifeLabel=self.labelLifeIA, y=0.03 , ventana=self.ventana ,nombre="Oponente")
       self.jugadores = [self.jugador1, self.jugadorIA]
       self.limpiar()
       self.placeLabelJugadores()
       self.setLabelAccion("Asignando cartas...")
       self.IA = ia(self)
       self.opcion = 0
       self.habilidadOp = ""
       self.jugadorTurno = 0
       self.cartas = []
       self.crearCartas()
   
    def iniciarJuego(self):
       self.setLabelAccion("")
       self.asignarCartas()
       self.placeLabelJugadores()
       self.colocarCartasPlayers()
       self.jugadores[self.jugadorTurno].turno=True
       self.mostrarOpciones()
       self.jugador1TurnoStart()
        
        # Colocar ciclo while para la IA
    def jugador1TurnoStart(self):
      if self.jugadores[self.jugadorTurno].turno:
       if self.opcion != 0:
             match self.opcion:
                case 1:
                   self.limpiar()
                   self.mostrarHabilidades()
                case 2:
                   self.jugadores[self.jugadorTurno].insertCard(self.cartas[0])
                   self.cartas.pop(0)
                   self.limpiar()
                   if(not self.jugador1.masoPerdido):
                    self.ventana.after(2000, lambda: self.mostrarOpciones())
                case 3:
                   self.limpiar()
                   self.jugadores[self.jugadorTurno].plantarse()
                        
             self.opcion = 0
       self.ventana.after(100, self.jugador1TurnoStart)
      else:
         if(self.jugador1.masoPerdido == False):
          print("Turno del oponente")
          self.setLabelAccion("Turno del oponente")
          self.setLabelAccionAfet("", 1500)
          self.jugadorTurno = 1
          self.jugadorIA.turno = True
          self.ventana.after(1750 , lambda: self.realizarAccionIA() )
         else:
            if not self.finJuego():
               self.finTurno()
            else: 
               self.finJuego()

    def realizarAccionIA(self):
     state = self.IA.reset()
     self.done = False
    
     def ejecutar_accion():
        if not self.done:
            action = self.IA.action_space.sample()
            state, reward, self.done, info = self.IA.step(action)
            if not self.done:
                self.ventana.after(2800, lambda: ejecutar_accion())  # Programar la próxima acción después de 2.6 segundos
            else:
                 if not self.finJuego():
                    self.ventana.after(2000, lambda: self.finTurno())
                 else:
                    self.ventana.after(2000, lambda: self.finJuego())
     ejecutar_accion()


    def usarHabilidadIA(self, i):
        print("IA usa habilidad")
        self.mostrarOpcionesIA(0, 500)
        self.ventana.after(1100, lambda: self.mostrarHabilidadesIA(i) )
        reward = 20
        return reward

    def tomarCartaIA(self):
        print(len(self.cartas))
        print("IA usa tomar carta")

        if len(self.cartas) > 0:
         self.mostrarOpcionesIA(1, 500)
         self.jugadores[self.jugadorTurno].insertCard(self.cartas[0])
         self.cartas.pop(0)
        reward = 10
        return reward

    def plantarseIA(self):
        print("Ia uso plantarse")
        self.mostrarOpcionesIA(2, 500)
        self.jugadorIA.plantarse()
        reward = 5
        return reward 

    def rondaReiniciar(self):
        for jugador in self.jugadores :
            jugador.vaciarMaso()
        self.cartas=[]    
        self.crearCartas()
        self.ventana.after(1100, lambda: self.limpiar())
        self.setLabelAccion("Asignando cartas...")
        self.opcion = 0
        self.jugadorTurno = 0
        self.ventana.after(2000, lambda: self.iniciarJuego())  # Espera 5 segundos antes de llamar a iniciarJuego

    def finTurno(self):
        resultado = ""
        if self.jugador1.getCountMaso() == self.jugadorIA.getCountMaso():
         resultado = "Empate"
        elif self.jugadorIA.getCountMaso() > self.jugador1.getCountMaso() and not self.jugadorIA.masoPerdido:
         resultado = "Perdiste la ronda"
         self.jugador1.popVida()
        elif self.jugador1.getCountMaso() > self.jugadorIA.getCountMaso() and not self.jugador1.masoPerdido:
         resultado = "Ganaste la ronda"
         self.jugadorIA.popVida()
        elif self.jugadorIA.masoPerdido:
         resultado = "Ganastes la ronda"
         self.jugador1.popVida()
        elif self.jugador1.masoPerdido:
         resultado = "Perdiste la ronda"
         self.jugador1.popVida()
        else:
         resultado = "Ninguno de los anteriores"

        self.setLabelAccionAfet(resultado, 1200)
        self.setLabelAccionAfet("", 2000)
        self.ventana.after(2500, lambda: self.rondaReiniciar())


    def finJuego(self):
        if self.jugadores[0].getCountVidas() == 0 :  
         self.setLabelAccion("Se termino el juego")
         self.setLabelAccionAfet("", 1500) 
         return True
        elif  self.jugadores[1].getCountVidas() == 0:
         self.setLabelAccion("Ganastes")
         self.setLabelAccionAfet("", 1500)
         return True
        return False
          
   
    def mostrarOpciones(self):
       buttonOp1 = Button(self.ventana, text="Habilidad", background=self.colorBotons, relief="raised", foreground="white" ,command=lambda: self.asignarOpcion(1), font=("arial", 11, "bold"), activebackground=self.colorAccion, activeforeground=self.activeForeground)
       buttonOp2 = Button(self.ventana, text="Tomar carta", background=self.colorBotons, relief="raised" , foreground="white" ,command=lambda: self.asignarOpcion(2), font=("arial", 11, "bold"), activebackground=self.colorAccion, activeforeground=self.activeForeground)
       buttonOp3 = Button(self.ventana, text="Plantarse", background=self.colorBotons, relief="raised", foreground="white" ,command=lambda: self.asignarOpcion(3), font=("arial", 11, "bold"), activebackground=self.colorAccion, activeforeground=self.activeForeground)
       buttonOp1.place(relx=0.30, rely=0.6, relwidth=0.13)
       buttonOp2.place(relx=0.46, rely=0.55, relwidth=0.14)
       buttonOp3.place(relx=0.62, rely=0.6, relwidth=0.13)

    def mostrarHabilidades(self):
      if(self.jugadores[self.jugadorTurno].getCountHabilidades() > 0):
       habilidadesJugador = self.jugador1.getHabilidades()
    
        # Definir las posiciones y tamaños de los botones
       posiciones = [
         {"relx": 0.30, "rely": 0.6, "relwidth": 0.13},
         {"relx": 0.46, "rely": 0.55, "relwidth": 0.14},
         {"relx": 0.60, "rely": 0.6, "relwidth": 0.13}
        ]
       
       # Crear los botones con sus respectivas habilidades
       buttonArray = [
          Button(self.ventana, background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold"), activebackground=self.colorAccion, activeforeground=self.activeForeground),
          Button(self.ventana, background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold"), activebackground=self.colorAccion, activeforeground=self.activeForeground),
          Button(self.ventana, background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold"), activebackground=self.colorAccion, activeforeground=self.activeForeground)
        ]

       # Colocar los botones utilizando las posiciones almacenadas
       for i in range(self.jugadores[self.jugadorTurno].getCountHabilidades()):
        buttonArray[i].place(relx=posiciones[i]["relx"], rely=posiciones[i]["rely"], relwidth=posiciones[i]["relwidth"])
        buttonArray[i].config(text=habilidadesJugador[i], command=self.handleClicHabilidad(habilidadesJugador[i], i))
      else:
         self.setLabelAccion("No tienes habilidades")
         self.setLabelAccionAfet("", 2000)
         self.mostrarOpciones()


    def mostrarOpcionesIA (self, index = -1, tiempo = 1100):
       buttonOp1 = Label(self.ventana, text="Habilidad", background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold"))
       buttonOp2 = Label(self.ventana, text="Tomar carta", background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold"))
       buttonOp3 = Label(self.ventana, text="Plantarse", background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold"))
       buttonOp1.place(relx=0.30, rely=0.2, relwidth=0.13)
       buttonOp2.place(relx=0.46, rely=0.35, relwidth=0.14)
       buttonOp3.place(relx=0.62, rely=0.2, relwidth=0.13)
       arrayButton = [buttonOp1, buttonOp2, buttonOp3]

       #  Marcar la opcion elegida por la IA 
       if(index != -1):
        self.ventana.after(tiempo , lambda: self.accionButton(arrayButton, index))
        self.ventana.after(1100, lambda: self.limpiar())

    def mostrarHabilidadesIA (self, index = -1):
      if(self.jugadores[1].getCountHabilidades() > 0):
       habilidadesJugador = self.jugadores[1].getHabilidades()
    
        # Definir las posiciones y tamaños de los botones
       posiciones = [
         {"relx": 0.30, "rely": 0.2, "relwidth": 0.13},
         {"relx": 0.46, "rely": 0.35, "relwidth": 0.14},
         {"relx": 0.60, "rely": 0.2, "relwidth": 0.13}
        ]
       
       # Crear los botones con sus respectivas habilidades
       buttonArray = [
          Label(self.ventana, background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold")),
          Label(self.ventana, background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold")),
          Label(self.ventana, background=self.colorBotons, relief="raised", foreground="white", font=("arial", 11, "bold"))
        ]

       # Colocar los botones utilizando las posiciones almacenadas
       for i in range(self.jugadores[1].getCountHabilidades()):
        buttonArray[i].place(relx=posiciones[i]["relx"], rely=posiciones[i]["rely"], relwidth=posiciones[i]["relwidth"])
        buttonArray[i].config(text=habilidadesJugador[i])
      
       if(index != -1):
        self.ventana.after(300, lambda: self.accionButton(buttonArray, index))
        self.ventana.after(320, self.handleClicHabilidad(habilidadesJugador[index], index, True))
        self.ventana.after(1100, lambda: self.limpiar())

      else:
         self.setLabelAccion("No tienes habilidades")
         self.setLabelAccionAfet("", 2000)
         self.mostrarOpcionesIA()


    def cartaSiguienteIA(self):
      self.verCartaSiguiente(True)


    def accionButton(self, arrayButton, index):
         arrayButton[index].config(background=self.colorAccion, foreground=self.activeForeground, relief="sunken")

    
    def escogerHabilidad(self, IA = False):
       if self.habilidadOp != "" :
        match self.habilidadOp:
            case "Vida":
              self.jugadores[self.jugadorTurno].putVida()
              if(IA == False):
               self.limpiar()       
               self.ventana.after(300, lambda: self.mostrarOpciones())
               self.habilidadOp = ""
            case "Quitar vida":
              if self.jugadorTurno > 0 :
               self.jugador1.popVida()
               self.habilidadOp = ""
              else :
               self.jugadores[self.jugadorTurno + 1].popVida()
               if(IA == False):
                self.limpiar()
                self.ventana.after(300, lambda: self.mostrarOpciones()) 
               self.habilidadOp = ""
            case "Sg. carta":
              if(IA == False):
                self.verCartaSiguiente()
                self.limpiar()
                self.ventana.after(300, lambda: self.mostrarOpciones()) 
              else:
                self.verCartaSiguiente(True)

    def verCartaSiguiente(self, IA = False):
        cartaSiguiente = self.cartas[0]
        valor = cartaSiguiente.valor
        tipo = cartaSiguiente.tipo
        if(not IA):
         self.setLabelAccion(str(valor) + ", " +  tipo )
         self.setLabelAccionAfet("", 1200)
        else:
           return cartaSiguiente
            
    def colocarLabelImp(self):
        colorLabelCount = "#cecece"
        self.ventana.config(background=self.colorUniversal)
        self.labelCountJugador = Label(self.ventana, text="0", background=colorLabelCount, font=("Arial", 12)) 
        self.labelCountIaJugador = Label(self.ventana, text="0", background=colorLabelCount, font=("Arial", 12))
        self.labelAccion = Label(self.ventana, text="", background=self.colorUniversal, font=("Arial", 12, "bold"), relief="ridge")
        self.ventana.config(background=None)
        self.labelLifeJugador = Label(self.ventana, text="Tus vidas: 3", background=self.colorUniversal, foreground="white"  ,font=("Arial", 12))
        self.labelLifeIA = Label(self.ventana, text="Oponente vidas: 3", background=self.colorUniversal, foreground="white" ,font=("Arial", 12))

    def placeLabelJugadores(self):
         self.labelCountJugador.place(relx=0.49, rely=0.7, relwidth=0.05, relheight=0.05)
         self.labelCountIaJugador.place(relx=0.49, rely=0.2, relwidth=0.05, relheight=0.05)
         self.labelLifeJugador.place(relx=0.8, rely=0.01, relwidth=0.2, relheight=0.05)
         self.labelLifeIA.place( relx=0 , rely=0.01 ,  relwidth=0.2, relheight=0.05)  
         self.labelAccion.place(relx=0.15, rely=0.4, relwidth=0.7, relheight=0.09)

    def crearCartas(self):
       for i in range(8):
        carta1 = carta(4,"Figura")
        self.cartas.append(carta1)

    def setLabelAccion(self, txt):
       if txt == "":
        self.labelAccion.config(text=txt, borderwidth=0)
       else:
         self.labelAccion.config(text=txt, foreground="white", borderwidth=1, border=2, relief="ridge") 
     
    def asignarOpcion(self, i):
       self.opcion = i
   
    def limpiar(self, playerCards = True):
        self.ventana.bind("<Configure>", None)
        labels = [self.labelCountJugador, self.labelCountIaJugador, self.labelAccion, self.labelLifeJugador, self.labelLifeIA]
        for widget in self.ventana.winfo_children():
         if widget not in labels:
            widget.destroy()
            # Para hacer herencia se coloca la clase nombre_clase (clase_herencia)
        if(playerCards):
           self.colocarCartasPlayers()

    def setLabelAccionAfet(self , text, time):
       self.ventana.after(time,  lambda: self.setLabelAccion(text))
   
    def accionAfter(self, funcion, time):
       self.ventana.after(time, lambda: funcion)

    def setHabilidadUse(self, text, index, IA = False):
       self.habilidadOp = text
       self.jugadores[self.jugadorTurno].popHabilidad(index)
       if(IA == True):
        self.escogerHabilidad(IA)
       else: 
         self.escogerHabilidad()

    def handleClicHabilidad(self, text, index, IA = False):
     return lambda: self.setHabilidadUse(text, index, IA)

    def asignarCartas(self):
         i = 0
         for ciclo in range(4):
             if(ciclo == 2):
                i=1
             self.jugadores[i].insertCard(self.cartas[0])
             self.cartas.pop(0)
      
    
    def colocarCartasPlayers(self):
      for jugador in self.jugadores:
           jugador.colocarCardsLabels()


 

 

       