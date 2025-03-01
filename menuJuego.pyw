from tkinter import Button, Tk, Label
from inicioJuego import inicioJuego
from PIL import Image, ImageTk

def handleButtonInicio():
    global ventana
    nuevoJuego = inicioJuego(ventana)
    ventana.after(2000, nuevoJuego.iniciarJuego)  # Espera 5 segundos antes de llamar a iniciarJuego

def handleButtonExit():
    global ventana
    ventana.quit()  

def on_enter(e):
    e.widget['background'] = 'yellow'
    e.widget['borderwidth'] = 1

def on_exit(e):
    e.widget['background'] = 'SystemButtonFace'
    e.widget['borderwidth'] = 0    

def redimensionar_imagen(event):
    global imagen_fondo, label_imagen
    nueva_ancho = event.width
    nueva_alto = event.height
    
    # Verificar que los valores de ancho y alto sean mayores que cero
    if nueva_ancho > 0 and nueva_alto > 0:
        imagen_redimensionada = imagen_original.resize((nueva_ancho, nueva_alto), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen_redimensionada)

        # Asegurarse de que label_imagen existe antes de configurarlo
        if label_imagen.winfo_exists():
            label_imagen.config(image=imagen_fondo)
            label_imagen.image = imagen_fondo

ventana = Tk()
ventana.title("BlackSkill")
ventana.resizable(1,1)
ventana.geometry("650x420")
ventana.config(bg=None)

# Cargar la imagen original
ruta_imagen = "img/bg-inicio.png"
imagen_original = Image.open(ruta_imagen)
imagen_fondo = ImageTk.PhotoImage(imagen_original)

# ventana.iconbitmap("") para colocar un nuevo icono den la ventana

# Crear un Label para contener la imagen
label_imagen = Label(ventana, image=imagen_fondo)
label_imagen.place(x=0, y=0, relwidth=1, relheight=1)

label_titulo = Label(ventana, text="BlackSkill", background="#003d36", foreground="white",font=("default", 18), relief="ridge" )
label_titulo.place(relx=0.8, rely=0.1, relwidth= 0.2, relheight=0.09)

buttonInicio = Button(ventana, text='Iniciar juego', command = handleButtonInicio, relief="flat")
buttonInicio.place(relx=0.01, rely=0.4, relwidth=0.2, relheight=0.05)

buttonSalir = Button(ventana, text='Salir de juego', command = handleButtonExit, relief="flat")
buttonSalir.place(relx=0.01, rely=0.5, relwidth=0.2, relheight=0.05)

# buttonInicio.bind("<Enter>", on_enter)
# buttonInicio.bind("<Leave>", on_exit)
# buttonSalir.bind("<Enter>", on_enter)
# buttonSalir.bind("<Leave>", on_exit)

ventana.bind("<Configure>", redimensionar_imagen)

ventana.mainloop()