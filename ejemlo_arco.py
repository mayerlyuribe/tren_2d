from tkinter import*

BASE=400
ALTURA=400

ventana=Tk()
ventana.title("ejemplos")
ventana.resizable(False,False)
ventana.geometry("500x500")
ventana.config(bg="black")
frame_graf=Frame(ventana, width=500,height=500)
frame_graf.config(bg="white", width=400, height=400)
frame_graf.place(x=50,y=50)
c = Canvas(frame_graf, width=BASE, height=ALTURA)
c.config(bg="plum1")
c.place(x=0, y=0)
rect1=c.create_rectangle(BASE/2-100,ALTURA,BASE/2+100,ALTURA/2+180,fill="black")
trian1=c.create_polygon(BASE/2-50,ALTURA-20,BASE/2+50,ALTURA-20,BASE/2,ALTURA/2,outline="black",fill="chocolate3")
arc1=c.create_arc(BASE/2-100,ALTURA/2-100,BASE/2+100,ALTURA/2+100, start=180, extent=60, fill="goldenrod1")
arc2=c.create_arc(BASE/2-100,ALTURA/2-100,BASE/2+100,ALTURA/2+100, start=60, extent=60, fill="goldenrod1")
arc3=c.create_arc(BASE/2-100,ALTURA/2-100,BASE/2+100,ALTURA/2+100, start=300, extent=60,fill="goldenrod1")
ventana.mainloop()