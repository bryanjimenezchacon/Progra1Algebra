# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:22:50 2016

@author: bryan
"""
from itertools import *
import numpy as np
#numeroCarreteras = int (input("Digite algo: ")) 
table = list(product([0, 1], repeat = 3))# 3 por ahora



r1 = [22,32.3,4.5,15]
r2 = [62,53,7,122]
r3 = [73.8,68,8,143]

tablacondiciones = []
tablacondiciones.append(r1)
tablacondiciones.append(r2)
tablacondiciones.append(r3)

x = np.matrix(table)
y = np.matrix(tablacondiciones)

tablaResultado = x * y

posiblesSoluciones = []
for i in range(0, len(tablaResultado)):
    posiblesSoluciones.append(True)

contador = 0
for i in range(0, len(tablaResultado)):#Evalua longitud
    if (tablaResultado.item(contador) < 80) or (tablaResultado.item(contador) > 140):
        posiblesSoluciones[i] = False

    contador += 4#Cantidad columnas

contador = 1
for i in range(0, len(tablaResultado)):#Evalua total
    
    if (tablaResultado.item(contador) >= 120):
        posiblesSoluciones[i] = False
        print(tablaResultado.item(contador)) 

    contador += 4#Cantidad columnas
   
contador = 2
for i in range(0, len(tablaResultado)):#Evalua tiempo
    if (tablaResultado.item(contador) > 20):
        posiblesSoluciones[i] = False

    contador += 4#Cantidad columnas
    
contador = 3
for i in range(0, len(tablaResultado)):#Evalua beneficiados
    if (tablaResultado.item(contador) <= 150):
        posiblesSoluciones[i] = False

    contador += 4#Cantidad columnas
   
print(posiblesSoluciones)
for i in range(0, len(posiblesSoluciones)):
    if posiblesSoluciones[i] == True:
        print(table[i])  
