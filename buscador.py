print ("*** buscador de palabras dentro de un archivo ***")
print ("*************************************************")
print ("")
palabra = raw_input("palabra a buscar ?? ")
archivo = raw_input("Archivo donde Buscar >> ")

repetidas = 0
f = open(archivo)
lines = f.readlines()
for line in lines:
    palabras = line.split(' ')
    for p in palabras:
        if p == palabra:-
            repetidas = repetidas+1

print ("la palabra \"{0}\" se repite {1} veces en el Archivo {2}".format(palabra, repetidas, archivo))
