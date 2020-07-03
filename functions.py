from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
from visionAPI import reconocer_caras
from clases import *
root = Tk()

root.title('canvas')

root.filename =  filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#"""[obtiene los datos de la imagen que obtiene roo.filename y lo guarda en un archivo.txt
#para separa la ubicación de la imagen de los demas datos]
#"""
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
    """[funcion que recorre linea por linea un archivo.txt]

    Args:
        n ([type:int]): [este es un puntero que se debe digitar con la cantidad de lineas que tiene el archivo.txt]
        archivo ([type:str]): [obtiene el nombre del archivo digitado al llamar la función para que se abra el forma de lectura]
        cacaracter([type:str-bytes]):[se le asignan los datos de la lectura de cada linea]

        return(respuesta):([type:list]):[retorna una lista con los datos de cada linea del archivo.txt]
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

"""[l es un string que obtiene la ubición de la imagen que se obtiene llamando la función de leeLineas]
"""
l=str(lee_Lineas(3,"archivo1.txt")[1])
   
def imprimir():
    """[Función que crea un archivo con los el nombre de la persona digitada en el Entry de etiquetar
    esta función es llamada al seleccionar el boton guardar]
    """
    dato=Nombre.get()
    #print(type(dato))
    textfile=open("dato.txt","tw")
    textfile.write(dato)
    textfile.close()

    textfile=open("dato.txt","a")
    textfile.write(".bin")
    textfile.close()

    textfile=open("dato.txt", "tr")
    registro=textfile.read()
    textfile.close()

    file=open(registro, "bw")
    guardarArchivo(ListaPersonas,file)
    file.close()
    



"""[permite que la ventana para mostar a imagen en la interfaz grafica tenga la opción de utilizar el scroll del mouse]
"""
scrollbary = Scrollbar(root)
scrollbary.pack( side = RIGHT, fill = Y )

scrollbarx = Scrollbar(root,orient=HORIZONTAL)
scrollbarx.pack( side = BOTTOM, fill = X )


# circulo
"""[Abre una ventana de interfaz grafica]
"""
canvas = Canvas(width=500, height=500, bg='white', xscrollcommand = scrollbarx.set, yscrollcommand = scrollbary.set)
canvas.pack(expand=YES, fill=BOTH)

scrollbary.config( command = canvas.yview )
scrollbarx.config( command = canvas.xview )

"""[crea una ventana de interfaz grafica adiccional para mostar las opciones de etiquetar a la persona de la imagen
o realizar una busqueda por nombre de otras imagenes ya etiquetadas]
"""
ventana=Tk()
ventana.title("Etiquetar-Buscar")
ventana.geometry('310x150')

lbl = Label(ventana, text="--------Etiquetar--------")
lbl.grid(column=1, row=0,padx=(20,5))

lbl = Label(ventana, text="Nombre")
lbl.grid(column=0, row=2,padx=(20,5))
Nombre = Entry(ventana,width=20)
Nombre.grid(column=1, row=2,padx=(0,10))

btn = Button(ventana, text="Guardar",command=imprimir)
btn.grid(column=2, row=2,padx=(10,10))


lbl = Label(ventana, text="--------Buscar--------")
lbl.grid(column=1, row=6,padx=(20,5))

lbl = Label(ventana, text="Nombre")
lbl.grid(column=0, row=8,padx=(20,5))
txt = Entry(ventana,width=20)
txt.grid(column=1, row=8,padx=(0,10))

btn = Button(ventana, text="Buscar")
btn.grid(column=2, row=8,padx=(10,10))



#lb_nombre=tk.Label(canvas,text="Nombre: ")
#lb_apellido1=tk.Label(canvas,text="Primer Apellido: ")
#lb_apellido2=tk.Label(canvas,text="Segundo Apellido: ")


##img = PhotoImage(file="flor.jpg") 
  
img = ImageTk.PhotoImage(Image.open(root.filename.name))
canvas.create_image(0,0, anchor=NW, image=img)

"""[llama al metodo reconocer_caras desde visionAPI.py para realizar el reconocimiento 
del rostro mostrado en la imagen con la ubicación anteriormente asignada a "l"]
"""
r=reconocer_caras(l)
print(r)
cont=0
d=len(r)

"""[realiza un ciclo para crear un recuadro sobre el o los rostros reconocidos en la imagen seleccinada]
"""
while cont<d:
    x1=(r[cont]["vertices"][0]["x"])
    y1=(r[cont]["vertices"][0]["y"])
    x2=(r[cont]["vertices"][2]["x"])
    y2=(r[cont]["vertices"][2]["y"])
    canvas.create_rectangle(x1, y1, x2, y2, width=5, fill='red', stipple="gray12")
    cont+=1

root.mainloop()
#ventana.mainloop()

