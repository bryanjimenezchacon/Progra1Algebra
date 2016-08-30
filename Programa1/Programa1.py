# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 09:53:25 2016

@author: bryan
"""

from openpyxl import *


wb = load_workbook(filename='Tabla.xlsx', read_only=True)
ws1 = wb['2011-2012'] # Nombre de la hoja del excel
ws2 = wb['2012-2013'] # Nombre de la hoja del excel
ws3 = wb['2013-2014'] # Nombre de la hoja del excel
ws4 = wb['2014-2015'] # Nombre de la hoja del excel
ws5 = wb['2015-2016'] # Nombre de la hoja del excel


##------------------ Lectura de hojas ------------------##
hoja1 = []
i, j = 0,0
for row in ws1.rows:
    hoja1.append([])
    for cell in row:
        hoja1[i].append(cell.value)     
        j += 1
    i += 1
    
hoja2 = []
i, j = 0,0
for row in ws2.rows:
    hoja2.append([])
    for cell in row:
        hoja2[i].append(cell.value)     
        j += 1
    i += 1
    
hoja3 = []
i, j = 0,0
for row in ws3.rows:
    hoja3.append([])
    for cell in row:
        hoja3[i].append(cell.value)     
        j += 1
    i += 1

hoja4 = []
i, j = 0,0
for row in ws4.rows:
    hoja4.append([])
    for cell in row:
        hoja4[i].append(cell.value)     
        j += 1
    i += 1
    
hoja5 = []
i, j = 0,0
for row in ws5.rows:
    hoja5.append([])
    for cell in row:
        hoja5[i].append(cell.value)     
        j += 1
    i += 1
##---------------------    Filtrado de equipos posibles         --------------------------------------##
    
equipos = [] #Todos los equipos de todas las tablas
equiposLista = [] #Lsita de equipos que han participado
equiposValidos = [] #Equipos que han participado en todas las temporadas

#Lee los equipos
for i in range(0, len(hoja1)):
    equipos.append(hoja1[i][0])

for i in range(0, len(hoja2)):
    equipos.append(hoja2[i][0])
    
for i in range(0, len(hoja3)):
    equipos.append(hoja3[i][0])
    
for i in range(0, len(hoja4)):
    equipos.append(hoja4[i][0])
    
for i in range(0, len(hoja5)):
    equipos.append(hoja5[i][0])
equipos.sort()

#Lista los equipos in repetir nombres
for i in range (0, len(equipos)):
    if equipos[i] not in equiposLista:
        equiposLista.append(equipos[i])


#Lista los equipos validos
for i in range (0, len(equiposLista)):
    if (equipos.count(equiposLista[i]) == 5):
        equiposValidos.append(equiposLista[i])

    
##Crear matrices con los datos de los equipos validos solamente
  
hoja1Validos = []
hoja2Validos = []
hoja3Validos = []
hoja4Validos = []
hoja5Validos = []

        
for i in range(0, len(equiposValidos)):
    for j in range (0,len(hoja1)):
        if equiposValidos[i] == hoja1[j][0]:
            #print(hoja1[j])
            hoja1Validos.append([])
            hoja1Validos[i] = (hoja1[j])
hoja1Validos.sort() 

for i in range(0, len(equiposValidos)):
    for j in range (0,len(hoja2)):
        if equiposValidos[i] == hoja2[j][0]:
            #print(hoja1[j])
            hoja2Validos.append([])
            hoja2Validos[i] = (hoja2[j])
hoja2Validos.sort() 

for i in range(0, len(equiposValidos)):
    for j in range (0,len(hoja3)):
        if equiposValidos[i] == hoja3[j][0]:
            #print(hoja1[j])
            hoja3Validos.append([])
            hoja3Validos[i] = (hoja3[j])
hoja3Validos.sort() 

for i in range(0, len(equiposValidos)):
    for j in range (0,len(hoja4)):
        if equiposValidos[i] == hoja4[j][0]:
            #print(hoja1[j])
            hoja4Validos.append([])
            hoja4Validos[i] = (hoja4[j])
hoja4Validos.sort() 

for i in range(0, len(equiposValidos)):
    for j in range (0,len(hoja5)):
        if equiposValidos[i] == hoja5[j][0]:
            #print(hoja1[j])
            hoja5Validos.append([])
            hoja5Validos[i] = (hoja5[j])
hoja5Validos.sort()        



##---------------------    Preguntas      --------------------------------------##

preguntas = []

#Crea una matriz para los resultados
for i in range(0, len(equiposValidos)):
    preguntas.append([])
    preguntas[i] = [equiposValidos[i]]
    for j in range(0,7):
        preguntas[i].append(0)
        
## Calcula la primera pregunta
for i in range(0, len(preguntas)):
    preguntas[i][1] += hoja1Validos[i][2] 
    preguntas[i][1] += hoja2Validos[i][2] 
    preguntas[i][1] += hoja3Validos[i][2] 
    preguntas[i][1] += hoja4Validos[i][2] 
    preguntas[i][1] += hoja5Validos[i][2] 
    
    ## Calcula la segunda pregunta
for i in range(0, len(preguntas)):
    preguntas[i][2] += hoja1Validos[i][3] 
    preguntas[i][2] += hoja2Validos[i][3] 
    preguntas[i][2] += hoja3Validos[i][3] 
    preguntas[i][2] += hoja4Validos[i][3] 
    preguntas[i][2] += hoja5Validos[i][3] 
    
        ## Calcula la tercera pregunta
for i in range(0, len(preguntas)):
    preguntas[i][3] += hoja1Validos[i][4] 
    preguntas[i][3] += hoja2Validos[i][4] 
    preguntas[i][3] += hoja3Validos[i][4] 
    preguntas[i][3] += hoja4Validos[i][4] 
    preguntas[i][3] += hoja5Validos[i][4] 
    
        ## Calcula la cuarta pregunta
for i in range(0, len(preguntas)):
    preguntas[i][4] += hoja1Validos[i][5] 
    preguntas[i][4] += hoja2Validos[i][5] 
    preguntas[i][4] += hoja3Validos[i][5] 
    preguntas[i][4] += hoja4Validos[i][5] 
    preguntas[i][4] += hoja5Validos[i][5] 

        ## Calcula la quinta pregunta
for i in range(0, len(preguntas)):
    preguntas[i][5] += hoja1Validos[i][6] 
    preguntas[i][5] += hoja2Validos[i][6] 
    preguntas[i][5] += hoja3Validos[i][6] 
    preguntas[i][5] += hoja4Validos[i][6] 
    preguntas[i][5] += hoja5Validos[i][6] 
    

        ## Calcula la sexta pregunta
for i in range(0, len(preguntas)):
    preguntas[i][6] += hoja1Validos[i][8] 
    preguntas[i][6] += hoja2Validos[i][8] 
    preguntas[i][6] += hoja3Validos[i][8] 
    preguntas[i][6] += hoja4Validos[i][8] 
    preguntas[i][6] += hoja5Validos[i][8] 
    
    ##FALTA LA SEPTIMA PREGUNTA, PREGUNTAR AL PROFE QUE ES EXACTAMENTE




##Calcula el mayor para la pregunta 1    
#guardar la lista de los valores
listaVictorias = []
maximosVictorias=""
for i in range(0, len(preguntas)):
    listaVictorias.append(preguntas[i][1])
    
maximoVic = max(listaVictorias)

for i in range (0, len(listaVictorias)):
    if (listaVictorias[i] == maximoVic):
        maximosVictorias += " / "  + preguntas[i][0] 

##Calcula el mayor para la pregunta 2   
#guardar la lista de los valores
listaEmpates = []
maximosEmpatadores=""
for i in range(0, len(preguntas)):
    listaEmpates.append(preguntas[i][2])
    
maximoEmpates = max(listaEmpates)

for i in range (0, len(listaEmpates)):
    if (listaEmpates[i] == maximoEmpates):
        maximosEmpatadores += " / "  + preguntas[i][0] 

##Calcula el mayor para la pregunta 3
#guardar la lista de los valores
listaDerrotas = []
maximosDerrotas=""
for i in range(0, len(preguntas)):
    listaDerrotas.append(preguntas[i][3])
    
maximoDerr = max(listaDerrotas)

for i in range (0, len(listaDerrotas)):
    if (listaDerrotas[i] == maximoDerr):
        maximosDerrotas += " / " + preguntas[i][0]
        
##Calcula el mayor para la pregunta 4
#guardar la lista de los valores
listaGolesFavor = []
maximosGolesFavor=""
for i in range(0, len(preguntas)):
    listaGolesFavor.append(preguntas[i][4])
    
maximoGF = max(listaGolesFavor)

for i in range (0, len(listaGolesFavor)):
    if (listaGolesFavor[i] == maximoGF):
        maximosGolesFavor += " / "  + preguntas[i][0]
        
##Calcula el mayor para la pregunta 5
#guardar la lista de los valores
listaGolesContra = []
menosGolesContra=""
for i in range(0, len(preguntas)):
    listaGolesContra.append(preguntas[i][5])
    
menosGE = min(listaGolesContra)

for i in range (0, len(listaGolesContra)):
    if (listaGolesContra[i] == menosGE):
        menosGolesContra += " / " + preguntas[i][0]
        
##Calcula el mayor para la pregunta 6
#guardar la lista de los valores
listaPuntos = []
maximosPuntos=""
for i in range(0, len(preguntas)):
    listaPuntos.append(preguntas[i][6])
    
maximoPuntos = max(listaPuntos)

for i in range (0, len(listaPuntos)):
    if (listaPuntos[i] == maximoPuntos):
        maximosPuntos += " / " + preguntas[i][0]

        

### ------------------------ ESCRIBE EL EXCEL ------------------------###
#Libro
wbFinal = Workbook()
#Worksheet
wsFinal = wbFinal.active

# Primera Fila
wsFinal.append(["Equipos", "Victorias", "Empates", "Derrotas", "GF", "GE", "PTS", "Pregunta7"])

#Matriz de resultados
for i in range(0, len(preguntas)):
    wsFinal.append(preguntas[i])
wsFinal.append(["", "", ""])
wsFinal.append(["Categoria", "Equipos", "Total"])
#                         Categoria/Nombres Equipos/ Total
wsFinal.append(["Mas Victorias:", maximosVictorias, maximoVic])
wsFinal.append(["Mas Empates:", maximosEmpatadores, maximoEmpates])
wsFinal.append(["Mas Derrotas:", maximosDerrotas, maximoDerr])
wsFinal.append(["Mas GF:", maximosGolesFavor, maximoGF])
wsFinal.append(["Menos GE:", menosGolesContra, menosGE])
wsFinal.append(["Mas Puntos:", maximosPuntos, maximoPuntos])
wsFinal.append(["Mas dif Puntos:", maximosEmpatadores, maximoEmpates])

# Guarda el archivo
wbFinal.save("Resultado.xlsx")

    