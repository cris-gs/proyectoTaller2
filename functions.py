from tkinter import * 
from tkinter import filedialog
from PIL import ImageTk
from PIL import Image
from visionAPI import reconocer_caras
root = Tk()
root.title('canvas')

root.filename =  filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
a=str(root.filename)
b=a.find("mode")
textfile=open("archivo1.txt","tw")
textfile.write(a)
textfile.seek(23)
textfile.write("\n")
textfile.seek(b-2)
textfile.write("\n")
textfile.close()
def leeLineas(n,archivo):
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

l=str(leeLineas(3,"archivo1.txt")[1])
print(l)

#print (root.filename.name)

scrollbary = Scrollbar(root)
scrollbary.pack( side = RIGHT, fill = Y )

scrollbarx = Scrollbar(root,orient=HORIZONTAL)
scrollbarx.pack( side = BOTTOM, fill = X )


# circulo
canvas = Canvas(width=500, height=500, bg='white', xscrollcommand = scrollbarx.set, yscrollcommand = scrollbary.set)
canvas.pack(expand=YES, fill=BOTH)

scrollbary.config( command = canvas.yview )
scrollbarx.config( command = canvas.xview )

##img = PhotoImage(file="flor.jpg")      
img = ImageTk.PhotoImage(Image.open(root.filename.name))
canvas.create_image(0,0, anchor=NW, image=img)      

#canvas.create_rectangle(100, 70, 500, 507, width=5, fill='red', stipple="gray12")
print(reconocer_caras(l))
root.mainloop()

