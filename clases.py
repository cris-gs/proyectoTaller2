from visionAPI import reconocer_caras
from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
from visionAPI import reconocer_caras
from tkinter import scrolledtext

"""[crea una ventana donde se le permite al usuario seleccionar la imagen deseada y esta es mostrada en pantalla]
"""
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
"__________________________________________________________________________________________________________________"
"""[Crea otra ventana para que el usuario puede guardar una imagen con un nombre o sin un nombre, tambien
tiene la opcion de buscar a las imagenaes guardadas anteriormente, tambien se muestran los resultados de la imagen
seleccionada en la ventana anterior]
"""
ventana=Tk()
ventana.title("Etiquetar-Buscar")
ventana.geometry('850x540')

lbl = Label(ventana, text="--------Etiquetar--------")
lbl.grid(column=1, row=0,padx=(10,10))

lbl = Label(ventana, text="Nombre")
lbl.grid(column=0, row=2,padx=(20,5))
n_etiquetar = Entry(ventana,width=20)
n_etiquetar.grid(column=1, row=2,padx=(0,10))

lbl = Label(ventana, text="--------Buscar--------")
lbl.grid(column=1, row=6,padx=(10,10))

lbl = Label(ventana, text="Nombre")
lbl.grid(column=0, row=8,padx=(20,5))
n_buscar = Entry(ventana,width=20)
n_buscar.grid(column=1, row=8,padx=(0,10))

"""[Extraela ubicaion de la imagen seleccionada y la almacena en un archivo temporal txt 
para separar la ubicacion de los demas datos que tiene la variable root.filename]
"""
a=str(root.filename)
b=a.find("mode")
textfile=open("ubicacion_temp.txt","tw")
textfile.write(a)
textfile.seek(23)
textfile.write("\n")
textfile.seek(b-2)
textfile.write("\n")
textfile.close()
"____________________________________________________________________________________________________________"
def lee_Lineas(n,archivo):
    """[funcion que permite recorrel el archivo txt temporal que se creo para separar la ubicacion de los demas
    datos asi extrayendo solamete la ubicacion de la imagen selecciona y asignadola a una variable]

    Args:
        n ([type:str]): [Esta es una varaible que se asigna al llamar la funcion, que es el numero de lineas que
        tiene el archivo txt que se lea y asi saber cauntas veces ralizar el ciclo de lectura]
        archivo ([type:str]): [este es el nombre del archivo que se debe abrir e igual mente es  una variable que
        obtiene el valor a la hora de llamar a la funcion]
    """
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
"_____________________________________________________________________________________________________________"
l=str(lee_Lineas(3,"ubicacion_temp.txt")[1])#l es una variable de la cual obtiene la ubicacion extraida al llamar las funcion lee_lineas
r=reconocer_caras(l)#obtine los resultados del metodo reconocer caras llamado desde visionAPI.py
cont=0#permite desplazarce por la lista r donde se encuentran los reconocimientos faciales
d=len(r)#optiene el numero de imagenes reconocidas
columna=12#variable utilizada para la ubicacion de la columna
cont1=1#variable utillizada para el identificar la imagen la cual se muestan los resultados de reconocimiento facial

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
    """[convierten el valor de reconocimiento de cada expresion facial a un str para luego concatenarce con el
    el nombre de cada una de estas expresiones al mostrarse en la ventana de la interfaz grafica]
    """
    v=str(cont1)
    v1=str(valor)
    v2=str(valor1)
    v3=str(valor2)
    v4=str(valor3)
    v5=str(valor4)
    v6=str(valor5)
    v7=str(valor6)
    """[muestra en la ventana de la interfaz grafica los el nombre de cada expresion y sus respectivos valores reconocidos]
    """
    lbl = Label(ventana, text="IMAGEN:\t"+v)
    lbl.grid(column=0, row=columna,padx=(10,10))

    lbl = Label(ventana, text="Alegria:\r"+v1)
    lbl.grid(column=1, row=columna,padx=(10,10))

    lbl = Label(ventana, text="Tristeza:\r"+v2)
    lbl.grid(column=2, row=columna,padx=(10,10))

    lbl = Label(ventana, text="Ira:\r"+v3)
    lbl.grid(column=3, row=columna,padx=(10,10))

    lbl = Label(ventana, text="Sorpresa:\r"+v4)
    lbl.grid(column=4, row=columna,padx=(10,10))

    lbl = Label(ventana, text="subexpuesta:\r"+v5)
    lbl.grid(column=5, row=columna,padx=(10,10))

    lbl = Label(ventana, text="Borrosa:\r"+v6)
    lbl.grid(column=6, row=columna,padx=(10,10))

    lbl = Label(ventana, text="Sombrero:\r"+v7)
    lbl.grid(column=7, row=columna,padx=(10,10))
    columna+=1
    cont+=1
    cont1+=1
class persona:
    """[se crea la clase persona con las variables nombre y ubicación de cada imagen que se
     etiquete en la intefz grafica]
    """
    nombre=None
    ubicacion=None
    def __init__(self,nombre,ubicacion):
        self.nombre=nombre
        self.ubicacion=ubicacion

class rostro:   
    """[se crea la clase persona con las variables de recuador donde se almacenaran los vertice de cada rostro
    reconocido, y la variable persona que se utilizara como puentero entre las dos clases]
    """
    recuadro=None
    persona=None
    def __init__(self,persona,recuadro):
        self.persona=persona
        self.recuadro=recuadro

def imprimir():
    """[esta funcion es creada para el boton guardar el cual sirve para guarda runa imagen creado
    un archivo txt llamado personas donde se encuentra la ubicaion de la imagen y el nombre con el}
    que se guardo esta, hay que recalcar que se permite guardar la imagen sin escribirle un nombre
    esta se guawrdara como "sin nombre". esta funcion tambien a la hora de seleccionar el boton guardar
    crea un recuadro al rededor del o los rostros reconocisdos en la imagen asegurandole al usuario
    que la imagen fue guardada ]
    """
    r=reconocer_caras(l)
    if r==[]:
        root.mainloop()
    else: 
        if n_etiquetar==None:
            p1=persona("Sin nombre",l) 
        else:
            n=n_etiquetar.get()
            p1=persona(n,l)
            listaPersonas=[p1]
            cont=0
            conti=0
            d=len(r)
            recuadro=[]
            r1=[]
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
                    f.writelines(p.ubicacion+"\n")
            except FileNotFoundError:
                f=open("personas.txt","tw")
                for p in listaPersonas:
                    f.writelines(p.nombre+"\n"+p.ubicacion+"\n")
                f.close()

                f=open("rostro.txt","tw")
                for r in listaRostros:
                    f.writelines(r.recuadro.__str__()+"\n")
                    f.writelines(l+"\n")
            f.close()
    
#Se intento realizar una funcion que realizara una busqueda por medio del nombre que el usuario digitara
# lamentablemente esta funcion no tubo exito con  el problema de realizar la apertura de la imagen esta si es encontrada
# pero no se puede abrir en una ventana de la interfaz grafica solo imprime la hubicacion y el nombre de esta en la terminal    
"""
def buscar():
    cont=0 
    lineasp=[]
    lineasr=[]
    lectura=open("personas.txt","tr")
    lineasp.append(lectura.read().splitlines())
    lectura.close()
    lectura=open("rostro.txt","tr")
    lineasr.append(lectura.read().splitlines())
    lectura.close()
    while cont<len(lineasp[0]):
        n=n_buscar.get()
        if lineasp[0][cont]==n:
            a=(lineasp[0].index(lineasp[0][cont]))
            print(a)
            b=lineasp[0][a+1]
            busqueda = Tk()
            busqueda.title("Busqueda")
            img = ImageTk.PhotoImage(Image.open(b))
            panel = Label(busqueda, image = img)
            panel.pack(side = "bottom", fill = "both", expand = "yes")
            busqueda.mainloop()
            lineasp[0].pop(a)
        cont+=1

"""
def buscar():
    cont=0 
    lineasp=[]
    lineasr=[]
    lectura=open("personas.txt","tr")
    lineasp.append(lectura.read().splitlines())
    lectura.close()
    lectura=open("rostro.txt","tr")
    lineasr.append(lectura.read().splitlines())
    lectura.close()
    while cont<len(lineasp[0]):
        n=n_buscar.get()
        if lineasp[0][cont]==n:
            a=(lineasp[0].index(lineasp[0][cont]))
            print("El nombre de la imagen buscada:",lineasp[0][a])
            print("La hubicaciion de la imagen:",lineasp[0][a+1])
            lineasp[0].pop(a)
        cont+=1       
btn = Button(ventana, text="Guardar",command=imprimir)
btn.grid(column=2, row=2,padx=(10,10))

btn = Button(ventana, text="Buscar",command=buscar)
btn.grid(column=2, row=8,padx=(10,10))


root.mainloop()




