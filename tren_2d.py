#--------------------
#-----tren-2-d-------
#--------------------


from tkinter import *
import random

#-----------------------
# variables globales
#-----------------------

BASE = 460
ALTURA = 320

#-----------------------
# ventana principal
#-----------------------
ventana_principal = Tk()
ventana_principal.title("Tren 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry(f"500x500")
ventana_principal.config(bg="white")

color= "#"
for i in range(6):
    color + random.choice("0123456789ABCDEF")
#-----------------------
# frame de graficación
#-----------------------
frame_graficacion = Frame(ventana_principal, width=480, height=340)
frame_graficacion.config(bg="purple2", width=480, height=340)
frame_graficacion.place(x=10, y=10)

# creación canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="plum1")
c.place(x=10, y=10)

#-----------------------
# frame controles
#-----------------------

frame_controles = Frame(ventana_principal, width=480, height=140)
frame_controles.config(bg="purple2", width=480, height=130)
frame_controles.place(x=10, y=360)
#--------------------------------
linea_vert=c.create_line(BASE/2,-ALTURA,BASE/2,ALTURA)
linea_horz=c.create_line(-BASE,ALTURA/2,BASE,ALTURA/2)
rectang=c.create_rectangle(BASE/2-120,ALTURA/2,BASE/2+60,ALTURA/2+60,fill="gray44")
rectang2=c.create_rectangle(BASE/2-30,ALTURA/2-55,BASE/2+45,ALTURA/2,fill="gray44")

# ruedas
rueda1=c.create_oval(BASE/2-120,ALTURA/2+40, BASE/2-70,ALTURA/2+90, outline="black",fill="gray")
rueda2=c.create_oval(BASE/2-50,ALTURA/2+40,BASE/2,ALTURA/2+90, outline="black",fill="gray")
rueda3=c.create_oval(BASE/2+10,ALTURA/2+40,BASE/2+60,ALTURA/2+90, outline="black",fill="gray")
rect1=c.create_rectangle(BASE/2-30,ALTURA/2-89,BASE/2+45,ALTURA/2-65,fill="gray")
#rect2=c.create_rectangle(BASE/2)
rectang3= c.create_rectangle(BASE/2-35,ALTURA/2-75,BASE/2+50,ALTURA/2-55, fill="gray")



# desplegar ventana
ventana_principal.mainloop()

