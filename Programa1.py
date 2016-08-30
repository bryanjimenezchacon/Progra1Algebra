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
##---------------------             --------------------------------------##
    
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

print(len(equiposLista))
print(equiposValidos)
    
    
    
    