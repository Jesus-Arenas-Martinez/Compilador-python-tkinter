import argparse
from tkinter import messagebox as MessageBox
import re


def L_numeros():
    Ln = re.compile(r'([-]?[0-9]+([.][0-9]+)?)')

    return Ln


def L_variavales():
    Ln = re.compile(r'([a-zA-Z_]+([0-9]+)?(_[0-9]+)?)')
    return Ln


Tipo_de_Dato = r'(AMD|RAM|ROM)'


def L_Declarar_var_int():
    Ln = re.compile(                           #
        r'(AMD)')
    return Ln


def L_main():

    Ln = re.compile(r'Encendido [(][)]{')
    return Ln


def L_main_end():
    Ln = re.compile(r'}')
    return Ln


def L_Imprime():
    Ln = re.compile(r'Teclado_on[(]([a-zA-Z_]+([0-9]+)?(_[0-9]+)?)[)];')
    return Ln


def L_Imprime_Cad():
    Ln = re.compile(r'Teclado_on[(]".+"[)];')
    return Ln


#---------------init



#-------main
parser = argparse.ArgumentParser()
parser.add_argument("-E", "--Executable",
                    help="Genra el nopbre del ejecutable", action="store_true")
parser.add_argument("-f", "--file", help="Ruta Y Nombre  del archivo")
args = parser.parse_args()


def ruta():
    return args.file


if args.file:
    programa = open(ruta(), 'r')
    instrcciones = []
    contenido = programa.read()
    programa.seek(0)
    numero_lineas = len(programa.readlines())
    programa.seek(0)

    Expeciones_list = []
    Expeciones_list.append(L_main())
    Expeciones_list.append(L_Declarar_var_int())
    Expeciones_list.append(L_Imprime())
    Expeciones_list.append(L_Imprime_Cad())
    Expeciones_list.append(L_main_end())
    contenid0_copia = contenido
    for exprecion_eva in range(5):
        exp_encotrada = re.search(Expeciones_list[exprecion_eva], contenido)
        instrcciones.append(exp_encotrada)
        #instrcciones.append(tex_en.gro)
        #print(type(tex_en.group()))
        #print(numero_lineas)
        #print(contenido)

        instrcciones[0]


    def numero():
        return instrcciones
    
    msj=str(numero())

    def test():
        MessageBox.showinfo("Hola!",msj)

    test()    
