from visionAPI import reconocer_caras
from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
from visionAPI import reconocer_caras
from tkinter import scrolledtext

root = Tk()
root.title('canvas')
root.filename =  filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
scrollbary = Scrollbar(root)
scrollbary.pack( side = RIGHT, fill = Y )

scrollbarx = Scrollbar(root,orient=HORIZONTAL)
scrollbarx.pack( side = BOTTOM, fill = X )

canvas = Canvas(width=500, height=500, bg='white', xscrollcommand = scrollbarx.set, yscrollcommand = scrollbary.set)
canvas.pack(expand=YES, fill=BOTH)


scrollbary.config( command = canvas.yview )
scrollbarx.config( command = canvas.xview )

img = ImageTk.PhotoImage(Image.open(root.filename.name))
canvas.create_image(0,0, anchor=NW, image=img)

ventana=Tk()
ventana.title("Etiquetar-Buscar")
ventana.geometry('510x350')

lbl = Label(ventana, text="--------Etiquetar--------")
lbl.grid(column=1, row=0,padx=(10,10))

lbl = Label(ventana, text="Nombre")
lbl.grid(column=0, row=2,padx=(20,5))
Npersona = Entry(ventana,width=20)
Npersona.grid(column=1, row=2,padx=(0,10))

lbl = Label(ventana, text="--------Buscar--------")
lbl.grid(column=1, row=6,padx=(10,10))

lbl = Label(ventana, text="Nombre")
lbl.grid(column=0, row=8,padx=(20,5))
txt = Entry(ventana,width=20)
txt.grid(column=1, row=8,padx=(0,10))

a=str(root.filename)
b=a.find("mode")
textfile=open("ubicacion.txt","tw")
textfile.write(a)
textfile.seek(23)
textfile.write("\n")
textfile.seek(b-2)
textfile.write("\n")
textfile.close()

def lee_Lineas(n,archivo):
    file=open(archivo,"tr")
    respuesta=list()
    while n>1:
        linea=""
        caracter=file.read(1)
        if caracter!="":
            while True:
                if caracter=="\n":
                    break
                else:
                    linea+=caracter
                caracter=file.read(1)
        if caracter!="":
            respuesta.append(linea)
        else:
            respuesta.append(None)
        n-=1
    file.close()   
    return(respuesta)

l=str(lee_Lineas(3,"ubicacion.txt")[1])
r=reconocer_caras(l)
cont=0
d=len(r)
p1=11
p2=12
p3=13
p4=14
p5=15
p6=16
p7=17
p8=18
cont1=1

while cont<d:
    #realiza un acumulador del puntaje por la emoción definida
    conteo=(r[cont]["face_expressions"]["joy_likelihood"])
    valor=0
    if conteo=="VERY_LIKELY":
        valor=valor+5
    elif conteo=="LIKELY":
        valor=valor+4
    elif conteo=="POSSIBLE":
        valor=valor+3
    elif conteo=="UNLIKELY":
        valor=valor+2
    elif conteo=="VERY_UNLIKELY":
        valor=valor+0
    valor=((valor/d)*20)
    conteo=(r[cont]["face_expressions"]["sorrow_likelihood"])
    valor1=0
    if conteo=="VERY_LIKELY":
        valor1=valor1+5
    elif conteo=="LIKELY":
        valor1=valor1+4
    elif conteo=="POSSIBLE":
        valor1=valor1+3
    elif conteo=="UNLIKELY":
        valor1=valor1+2
    elif conteo=="VERY_UNLIKELY":
        valor1=valor1+0
    valor1=((valor1/d)*20)
    conteo=(r[cont]["face_expressions"]["anger_likelihood"])
    valor2=0
    if conteo=="VERY_LIKELY":
        valor2=valor2+5
    elif conteo=="LIKELY":
        valor2=valor2+4
    elif conteo=="POSSIBLE":
        valor2=valor2+3
    elif conteo=="UNLIKELY":
        valor2=valor2+2
    elif conteo=="VERY_UNLIKELY":
        valor2=valor2+0
    valor2=((valor2/d)*20)
    conteo=(r[cont]["face_expressions"]["surprise_likelihood"])
    valor3=0
    if conteo=="VERY_LIKELY":
        valor3=valor3+5
    elif conteo=="LIKELY":
        valor3=valor3+4
    elif conteo=="POSSIBLE":
        valor3=valor3+3
    elif conteo=="UNLIKELY":
        valor3=valor3+2
    elif conteo=="VERY_UNLIKELY":
        valor3=valor3+0
    valor3=((valor3/d)*20)
    conteo=(r[cont]["face_expressions"]["under_exposed_likelihood"])
    valor4=0
    if conteo=="VERY_LIKELY":
        valor4=valor4+5
    elif conteo=="LIKELY":
        valor4=valor+4
    elif conteo=="POSSIBLE":
        valor4=valor4+3
    elif conteo=="UNLIKELY":
        valor4=valor4+2
    elif conteo=="VERY_UNLIKELY":
        valor4=valor4+0
    valor4=((valor4/d)*20)
    conteo=(r[cont]["face_expressions"]["blurred_likelihood"])
    valor5=0
    if conteo=="VERY_LIKELY":
        valor5=valor5+5
    elif conteo=="LIKELY":
        valor5=valor5+4
    elif conteo=="POSSIBLE":
        valor5=valor5+3
    elif conteo=="UNLIKELY":
        valor5=valor5+2
    elif conteo=="VERY_UNLIKELY":
        valor5=valor5+0
    valor5=((valor5/d)*20)
    conteo=(r[cont]["face_expressions"]["headwear_likelihood"])
    valor6=0
    if conteo=="VERY_LIKELY":
        valor6=valor6+5
    elif conteo=="LIKELY":
        valor6=valor6+4
    elif conteo=="POSSIBLE":
        valor6=valor6+3
    elif conteo=="UNLIKELY":
        valor6=valor6+2
    elif conteo=="VERY_UNLIKELY":
        valor6=valor6+0
    valor6=((valor6/d)*20)

    lbl = Label(ventana, text="__________________Resultados__________________")
    lbl.grid(column=1, row=10,padx=(10,10))
    v=str(cont1)
    v1=str(valor)
    v2=str(valor1)
    v3=str(valor2)
    v4=str(valor3)
    v5=str(valor4)
    v6=str(valor5)
    v7=str(valor6)
  
    lbl = Label(ventana, text="IMAGEN:\t"+v)
    lbl.grid(column=0, row=p1,padx=(10,10))

    lbl = Label(ventana, text="Alegria:\r"+v1)
    lbl.grid(column=1, row=p2,padx=(10,10))

    lbl = Label(ventana, text="Tristeza:\r"+v2)
    lbl.grid(column=1, row=p3,padx=(10,10))

    lbl = Label(ventana, text="Ira:\r"+v3)
    lbl.grid(column=1, row=p4,padx=(10,10))

    lbl = Label(ventana, text="Sorpresa:\r"+v4)
    lbl.grid(column=1, row=p5,padx=(10,10))

    lbl = Label(ventana, text="subexpuesta:\r"+v5)
    lbl.grid(column=1, row=p6,padx=(10,10))

    lbl = Label(ventana, text="Borrosa:\r"+v6)
    lbl.grid(column=1, row=p7,padx=(10,10))

    lbl = Label(ventana, text="Sombrero:\r"+v7)
    lbl.grid(column=1, row=p8,padx=(10,10))
    p1+=8
    p2+=8
    p3+=8
    p4+=8
    p5+=8
    p6+=8
    p7+=8
    p8+=8

    cont+=1
    cont1+=1
class persona:
    nombre=None
    ubicacion=None
    def __init__(self,nombre,ubicacion):
        self.nombre=nombre
        self.ubicacion=ubicacion

class rostro:
    recuadro=None
    persona=None
    def __init__(self,persona,recuadro):
        self.persona=persona
        self.recuadro=recuadro

def imprimir():
    r=reconocer_caras(l)
    if r==[]:
        root.mainloop()
    else: 
        if Npersona==None:
            p1=persona("Sin nombre",l) 
        else:
            n=Npersona.get()
            p1=persona(n,l)
            listaPersonas=[p1]
            cont=0
            conti=0
            d=len(r)
            recuadro=[]
            while cont<d:
                recuadro.append([r[cont]["vertices"][0],r[cont]["vertices"][2]])
                r1=rostro(listaPersonas[0],recuadro)
                cont+=1
            while conti<len(recuadro):
                x1=(recuadro[conti][0]["x"])
                y1=(recuadro[conti][0]["y"])
                x2=(recuadro[conti][1]["x"])
                y2=(recuadro[conti][1]["y"])
                canvas.create_rectangle(x1, y1, x2, y2, width=5, fill='red', stipple="gray12")
                conti+=1  
            print(recuadro)

            listaRostros=[r1]
            try:
                f=open("personas.txt","a")
                for p in listaPersonas:
                    f.writelines(p.nombre+"\n"+p.ubicacion+"\n")
                f.close()

                f=open("rostro.txt","a")
                for r in listaRostros:
                    f.writelines(r.recuadro.__str__()+"\n")
                    f.writelines(listaPersonas.index(r.persona).__str__()+"\n")
            except FileNotFoundError:
                f=open("personas.txt","tw")
                for p in listaPersonas:
                    f.writelines(p.nombre+"\n"+p.ubicacion+"\n")
                f.close()

                f=open("rostro.txt","tw")
                for r in listaRostros:
                    f.writelines(r.recuadro.__str__()+"\n")
                    f.writelines(listaPersonas.index(r.persona).__str__()+"\n")
            f.close()
            
           




btn = Button(ventana, text="Guardar",command=imprimir)
btn.grid(column=2, row=2,padx=(10,10))

btn = Button(ventana, text="Buscar")
btn.grid(column=2, row=8,padx=(10,10))



root.mainloop()

"""
recuadro=[r[1]["vertices"][0],r[1]["vertices"][1]]
r2=rostro(listaPersonas[1],recuadro)
recuadro=[r[2]["vertices"][0],r[2]["vertices"][1]]
r3=rostro(listaPersonas[2],recuadro)
"""





