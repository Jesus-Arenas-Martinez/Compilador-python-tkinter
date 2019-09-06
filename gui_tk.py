from tkinter import *
from tkinter import filedialog
import os
import re 
from lp import *
from functools import partial

raiz=Tk()
dicc_palabras = {
    1: ['ROM', ''],
    2: ['Teclado_on', ''],
    3: ['Encendido', ''],
    4: ['AMD', ''],
    5: ['Disco', ''],
    6: ['cpu', ''],
    7: ['Bocina', ''],
    8: ['Fin', ''],
    9: ['RAM', ''],
    10: ['AGP', ''],
    11:['=',''],
        12:['<',''],
        13:['>',''],
        14:['<=',''],
        15:['>=',''],
        16:['==',''],
        17:['+',''],
        18:['-',''],
        19:['*',''],
        20:['/',''],
        21:[';',''],
        22:[',','']     
}

def resaltar_palabra(_Text, _num_lin, _dicc_palabras,color2):
        dicc_palabras_int = {
        1: ['ROM', ''],
        2: ['Teclado_on', ''],
        3: ['Encendido', ''],
        4: ['AMD', ''],
        5: ['Disco', ''],
        6: ['cpu', ''],
        7: ['Bocina', ''],
        8: ['Fin', ''],
        9: ['RAM', ''],
        10: ['AGP', '']
        }
        dicc_arit={
        1:['+',''],
        2:['-',''],
        3:['*',''],
        4:['/','']
        }
        dicc_signos={
        1:['=',''],
        2:['<',''],
        3:['>',''],
        4:['<=',''],
        5:['>=',''],
        6:['==','']       
        }
        dicc_fin={
        1:[';','']
        }
        _dicc_i = 0
        bg_color = color2
        tag_reservadas = '1'
        tag_signos='2'
        tag_arit='3'
        tag_fin='4'
        tag_coma='5'
        for _k_ in _dicc_palabras:

                palabra = _dicc_palabras[_k_][_dicc_i] 
                #print(palabra)
                palabra_len = len(palabra)
               # print(palabra_len)
                index = '1.0'
                while True:
                        plbra_i = _Text.search(palabra, index, stopindex=END)
                       
                        if not plbra_i:
                                break
                        
                        plbra_i_ini = int(plbra_i.split('.')[0])
                        plbra_i_fin = int(plbra_i.split('.')[1]) + palabra_len
                        coords = '{}.{}'.format(plbra_i_ini, plbra_i_fin)
                        
                        for _s_ in dicc_signos:
                                
                                if palabra == dicc_signos [_s_][_dicc_i]:
                                        
                                        _Text.tag_add(tag_signos,plbra_i,coords)
                                        _Text.tag_configure(
                                        tag_signos, foreground='purple', font='helvetica 20 bold')
                        
                        for _s_ in dicc_palabras_int:
                                if palabra == dicc_palabras_int [_s_][_dicc_i]:
                                        _Text.tag_add(tag_reservadas, plbra_i, coords)
                                        
                                        _Text.tag_configure(
                                        tag_reservadas, foreground=bg_color, font='helvetica 20 bold')
                        for _s_ in dicc_arit:
                                if palabra == dicc_arit [_s_][_dicc_i]:
                                        _Text.tag_add(tag_arit, plbra_i, coords)
                                        
                                        _Text.tag_configure(
                                        tag_arit, foreground="yellow", font='helvetica 20 bold')                
                        for _s_ in dicc_fin:
                                if palabra == dicc_fin [_s_][_dicc_i]:
                                        _Text.tag_add(tag_fin, plbra_i, coords)
                                        print ("coma--")
                                        _Text.tag_configure(
                                        tag_fin, foreground="blue", font='helvetica 20 bold')
                        if palabra == ',':
                                _Text.tag_add(tag_coma, plbra_i, coords)
                                print ("coma--")
                                _Text.tag_configure(
                                tag_coma, foreground="pink", font='helvetica 20 bold')        
                        index = coords

raiz.title("Coipilador Tesjo"+os.getcwd())
entrada = StringVar()
def Compilar():
        try:
                os.system("python3 lp.py -f "+fichero)
        except :
                os.system("python3 lp.py -f "+fichero2)
        
        


Frame1 = Frame()
textCodigo = Text(Frame1, width=140, height=40)
txt_ini_num_lin1 = int(textCodigo.index('end-1c').split('.')[0])

def abrirArch():
    global fichero
    fichero=filedialog.askopenfilename(title="Abir",initialdir="/Users/jesus/desktop",filetypes=(("Ficheros Tesjo", "*.tesjo"),
    ("ftext","*.txt")))
    programa = open(fichero, 'r')
    cod=programa.read()
    textCodigo.insert(INSERT,cod)
    
    txt_ini_num_lin = textCodigo.index('end-1c').split('.')[0]
    l1=int(txt_ini_num_lin)   
    for Linea in range(l1):
        linenumbers.config(state="normal")
        linenumbers.insert(INSERT, str(Linea)+"\n")
        linenumbers.config(state="disabled")

    resaltar_palabra(textCodigo,txt_ini_num_lin1, dicc_palabras,'green')

    

def GuardarArch():
        global fichero2
        fichero2=filedialog.asksaveasfilename(title="Abir",initialdir="/Users/jesus/desktop",filetypes=(("Fichero2s Tesjo", "*.tesjo"),
                                                                                                      ("ftext", "*.txt")))
        print(fichero2)
        archivo=open(fichero2,'w')
        archivo.write(textCodigo.get(1.0, 'end-1c'))
        archivo.close()
        
        
       
#------menu
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
barramenu=Menu(raiz)
raiz.config(menu=barramenu)

archivoMenu= Menu (barramenu)
archivoMenu.add_command(label="Guardar",command=GuardarArch)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir",command=abrirArch)
archivoMenu.add_command(label="salir :)")

barramenu.add_cascade(label="Archivo",menu=archivoMenu)  

archivoHerramientas=Menu(barramenu)
archivoHerramientas.add_command(label="Compilar")
archivoHerramientas.add_command(label="Ejecutar XD")

barramenu.add_cascade(label="Herramientas",menu=archivoHerramientas)

archivoAyuda=Menu(barramenu)
archivoAyuda.add_command(label="info")

barramenu.add_cascade(label="Ayuda",menu=archivoAyuda)
#------------------Sintaxix-------------------


def comSintaxis(_Text=textCodigo):
        Variables_dec=L_main();
        print(Variables_dec)
        com=_Text.get(1.0, 'end-1c')

        res=Variables_dec.match(com)
        if res != None:
                MessageBox.showinfo("Sintaxis","sintaxix corracta")
        else:
                MessageBox.showinfo("Sintaxis","sintaxix incorracta")        
        
        print (res)
        
        
#----fin---menu


Frame1.config(width=screen_width,height=screen_height,bg="black")
Frame1.pack(fill="both",expand="True")

btnCompila=Button(Frame1)
photoCompila = PhotoImage(file="/Volumes/APPS/Descargas/play1.gif")
btnCompila.config(image=photoCompila, width="40", height="25", activebackground="black",command=Compilar)
btnCompila.grid(row=1,column=1,padx=5,pady=5)
Btn_sintaxix=Button(Frame1,text="Compilar", activebackground="green",command=  comSintaxis)
Btn_sintaxix.grid(row=1,column=2,padx=5,pady=5)




textCodigo.grid(row=2, column=2, padx=5, pady=5)

scrollVert=Scrollbar(Frame1,command=textCodigo.yview)
scrollVert.grid(row=2,column=3,sticky="nsew")
textCodigo.config(font='helvetica 20 bold',fg="white", bg="black", yscrollcommand=scrollVert.set, insertbackground="white")



##--- funcion on ente 
def onEnter(event):
    linesN()
def linesN():
    linenumbers.config(font='helvetica 20 bold',state="normal")
    txt_ini_num_lin = textCodigo.index('end-1c').split('.')[0]
    linenumbers.insert(INSERT,txt_ini_num_lin+"\n")
    linenumbers.config(state="disabled")
def run_color(event):
        resaltar_palabra(textCodigo, txt_ini_num_lin1, dicc_palabras,'green')
       



linenumbers = Text(Frame1, width=3)
linenumbers.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
linenumbers.tag_configure('line', justify='right')
linenumbers.config(state="disabled")
linenumbers.config(fg="red", bg="black", yscrollcommand=scrollVert.set)
#linenumbers.config(state="disabled")

textCodigo.bind('<Return>',onEnter)
textCodigo.bind('<Key>',run_color)
'''
milabel = Label (Frame1,text="Label")
milabel.place(x=100,y=200)
'''

raiz.mainloop()
