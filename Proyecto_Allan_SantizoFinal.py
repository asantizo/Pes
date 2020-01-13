#!/usr/bin/env python
# coding: utf-8

# # Proyecto I
# Curso: Programación I
# 
# Profesor: Rodrigo Chang
# 
# Profesor auxiliar: Mauricio Vargas
# 
# $Allan$ $Fernando$  $Santizo$ $Flores$

# #### Juego de la vida de Conway
# Se trata de un juego de cero jugadores, lo que quiere decir que su evolución está determinada por el estado inicial y no necesita ninguna entrada de datos posterior. El "tablero de juego" es una malla plana formada por cuadrados (las "células") que se extiende por el infinito en todas las direcciones. Por tanto, cada célula tiene 8 células "vecinas", que son las que están próximas a ella, incluidas las diagonales. Las células tienen dos estados: están "vivas" o "muertas" (o "encendidas" y "apagadas"). El estado de las células evoluciona a lo largo de unidades de tiempo discretas (se podría decir que estos corresponden a los turnos). El estado de todas las células se tiene en cuenta para calcular el estado de las mismas al turno siguiente. Todas las células se actualizan simultáneamente en cada turno, siguiendo estas reglas: 
# 
# 1. Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
# 
# 2. Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación").
# 

# ### Funciones

# In[2]:


#Funciones

"""
En esta área se definen las funciones que serán llamadas en el programa

"""

#Tablero inicial, se define la función que tendra por argumento el tablero inicial y las condiciones iniciales inicial del juego
def tableroInicial(tablero,pares):
    for i in range(len(pares)):
        tablero[pares[i][0]][pares[i][1]] = 1
    return tablero

#Vecindad es una función que toma el tablero de salida y valida el entorno de cada una de las posiciones en la matriz
def vecindad(tableroSalida): 
    sumar={}
    for i in range(1,int(filas)+1):
        for h in range(1,int(columnas)+1):
            suma=tableroSalida[i-1][h-1]+tableroSalida[i-1][h]+tableroSalida[i-1][h+1]            +tableroSalida[i][h-1]+tableroSalida[i][h+1]            +tableroSalida[i+1][h-1]+tableroSalida[i+1][h]+tableroSalida[i+1][h+1]
            
            sumar[i,h]=suma
    return sumar

#Reglas define la función prinncipal del juego
def reglas(tableroSalida):

    for i in range(1,int(filas)+1):
            for h in range(1,int(columnas)+1):

                if tableroSalida[i][h] == 0 and sumar[i,h]==3:
                    t[i][h]=1

                elif tableroSalida[i][h] == 1:
                    if 2<=sumar[i,h]<4:
                        t[i][h]=1
                    else:
                        t[i][h]=0
    return t

#Define la función que hace la animación
def animacion(tablero):
    
    for m in range (len(tablero)):
        for n in range (len(tablero[0])):
            if tablero[m][n]==0:
                tablero[m][n]=' '
            else:
                tablero[m][n]='*'
    
    for fila in tablero:
        print(''.join([str(x) for x in fila]))
    print('')

#Define la función que quita deshace la animación
def deshacer(tablero):
    for m in range (len(tablero)):
        for n in range (len(tablero[0])):
            if tablero[m][n]=="*":
                tablero[m][n]=1
            else:
                tablero[m][n]=0
#Define la función que hace el conteo poblacional
def poblacion(tablero):
    sumaTotal = []
    for m in range (len(tablero)):
        sumaparcial=sum(tablero[m])
        sumaTotal.append(sumaparcial)
    pob = sum(sumaTotal)
    diccionario[repeticiones] = pob
    pob = ''

#Define la función que exporta el archivo de texto
def tabla_salida():
    with open('Allan_Santizo.txt', mode='w') as salida:
        escritura = csv.writer(salida, delimiter=',', quotechar='"')
        escritura.writerow(["Tiempo", "Población"])
        for key, values in diccionario.items():
            escritura.writerow([key, values])

#Se importan los modulos a utilizar en el programa
import os #Importa funciones del sistema operativo, para limpiar la pantalla
import time #Para poder establecer el tiempo que se muestra la matriz
import csv #Para poder exportar el archivo de texto
            


# ### Programa

# In[3]:


#Programa

"""
En esta área se se define el programa del juego

"""

#Extrae el archivo de texto
#f=open("aaa.txt","r") #Abre el archivo e imprime el contenido (archivo, modo lectura)
f=open(input('Ingrese nombre del archivo: ')+'.txt',"r") #Abre el archivo e imprime el contenido (archivo, modo lectura)

#input("Ingrese condiciones iniciales: "))+".txt"
t=f.readlines()#Devuelve todas las filas del archivo como una lista donde cada fila del archivo es un elemento

#se define la fila,columna y tiempo a partir de remover el texto basura y separar por comas
filas, columnas, tiempo = t[0].strip('\n').split(",")

#se crea en una lista los pares de las condiciones iniciales
pares = [] #Lista donde se asignaran los pares
for i in range(1,len(t)):#considerando cada elemento de t del 1 al final(0 define f,c,t)
    pares.append([int(elem) for elem in t[i].strip('\n').split(',')])
    #agrega a la lista los pares de la condición inicial

#Crea tablero
tablero = [[ 0 for n in range(int(columnas)+2)] for m in range(int(filas)+2)] #crea el tablero con "0" en columnas y número de filas se le adicionan dos para no tener problemas con las orillas


tableroSalida=tableroInicial(tablero,pares)
for i in tableroSalida: #Para cada elemento del tab
    print(''.join([str(x) for x in i]))
print("\n")
    
repeticiones=0 #Contador de la cantidad de repeticiones

diccionario={} #Diccionario que asigna las sumas realizadas en el entorno

while repeticiones < int(tiempo): #Repite el proceso la cantidad de periodos asignados en las condiciones iniciales
    
    tableroTemporal=tableroSalida.copy() #Realiza la copia del tablero salida
    t=tableroTemporal#Tablero temporal con cambios
    
    sumar= vecindad(tableroSalida)#Llama a la función que realiza las verificaciones de las sumas

    temporal=reglas(tableroSalida)#Llama la función que aplica las reglas del juego
    
    repeticiones= repeticiones + 1  #tablero salida
    tableroSalida=temporal #Asigna el tablero de salida para impresión
    
    animacion(temporal)#cambia e imprime la salida
    
    time.sleep(0.5) #posibilidad de hacer delay
    os.system("cls") #limpia la imagen para parar al próximo
    
    deshacer(temporal) #Quita la animación
    poblacion(temporal)#Ejecuta el conteo de la población
    
tabla_salida()

