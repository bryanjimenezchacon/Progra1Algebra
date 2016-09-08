# -*- coding: utf-8 -*-
"""

"""

import sys
from PyQt4 import QtCore, QtGui, uic
from openpyxl import *
from itertools import *
import numpy as np

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("InterfazMenu.ui")[0]
ruta = ""
fichero_actual = ""

class Principal(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
  QtGui.QMainWindow.__init__(self, parent)
  self.setupUi(self)
  self.buttonSeleccionarExcel.clicked.connect(self.abrirExcel)
  self.buttonCalcularCarretera.clicked.connect(self.calCarreteras)

    
  self.doubleSpinBoxLC1.setVisible(False)
  self.doubleSpinBoxCosC1.setVisible(False)
  self.doubleSpinBoxTC1.setVisible(False)
  self.doubleSpinBoxPC1.setVisible(False)
   
  
  self.spinBoxCantCarreteras.valueChanged.connect(self.agregarCarreteras)
  self.agregarCarreteras()
  self.connect(self.comboBoxL, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.cambiarSpinboxL)
  self.connect(self.comboBoxCos, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.cambiarSpinboxCos)
  self.connect(self.comboBoxT, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.cambiarSpinboxT)
  self.connect(self.comboBoxP, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.cambiarSpinboxP)

 ## Modifica la interfaz para las condiciones segun lo seleccionado 
 def cambiarSpinboxL(self, v):#Para variable de Longitud
     if v == "L > C" or v == "L >= C":
         self.doubleSpinBoxLC1.setVisible(False)
         
         self.doubleSpinBoxLC2.setVisible(True)
        
     elif v == "L < C" or v == "L <= C":
         self.doubleSpinBoxLC1.setVisible(True)
         
         self.doubleSpinBoxLC2.setVisible(False)
   
     else:
         self.doubleSpinBoxLC1.setVisible(True)
         self.doubleSpinBoxLC2.setVisible(True)
        # self.labelLC1.setVisible(True)
         #self.labelLC2.setVisible(True)
         
 def cambiarSpinboxCos(self, v):#Para variable de Costo
     if v == "Cos > C" or v == "Cos >= C":
         self.doubleSpinBoxCosC1.setVisible(False)
         self.doubleSpinBoxCosC2.setVisible(True)
         #self.labelCosC1.setVisible(False)
         #self.labelCosC2.setVisible(True)
     elif v == "Cos < C" or v == "Cos <= C":
         self.doubleSpinBoxCosC1.setVisible(True)
         self.doubleSpinBoxCosC2.setVisible(False)
         #self.labelCosC1.setVisible(True)
         #self.labelCosC2.setVisible(False)
     else:
         self.doubleSpinBoxCosC1.setVisible(True)
         self.doubleSpinBoxCosC2.setVisible(True)
         #self.labelCosC1.setVisible(True)
         #self.labelCosC2.setVisible(True)
         
 def cambiarSpinboxT(self, v):#Para variable de Tiempo
     if v == "T > C" or v == "T >= C":
         self.doubleSpinBoxTC1.setVisible(False)
         self.doubleSpinBoxTC2.setVisible(True)
         #self.labelTC1.setVisible(False)
         #self.labelTC2.setVisible(True)
     elif v == "T < C" or v == "T <= C":
         self.doubleSpinBoxTC1.setVisible(True)
         self.doubleSpinBoxTC2.setVisible(False)
         #self.labelTC1.setVisible(True)
         #self.labelTC2.setVisible(False)        
     else:
         self.doubleSpinBoxTC1.setVisible(True)
         self.doubleSpinBoxTC2.setVisible(True)
         #self.labelTC1.setVisible(True)
         #self.labelTC2.setVisible(True)
         
 def cambiarSpinboxP(self, v):#Para variable de Poblacion
     if v == "P > C" or v == "P >= C":
         self.doubleSpinBoxPC1.setVisible(False)
         self.doubleSpinBoxPC2.setVisible(True)
         #self.labelPC1.setVisible(False)
         #self.labelPC2.setVisible(True)
     elif v == "P < C" or v == "P <= C":
         self.doubleSpinBoxPC1.setVisible(True)
         self.doubleSpinBoxPC2.setVisible(False)
         #self.labelPC1.setVisible(True)
         #self.labelPC2.setVisible(False)         
     else:
         self.doubleSpinBoxPC1.setVisible(True)
         self.doubleSpinBoxPC2.setVisible(True)
         #self.labelPC1.setVisible(True)
        # self.labelPC2.setVisible(True)   
         
 def abrirExcel(self):#Para el programa 1
    nombre_fichero = QtGui.QFileDialog.getOpenFileName(self, "Abrir Excel", ruta)
    if nombre_fichero:
        self.fichero_actual = nombre_fichero
        Programa1.procesar(nombre_fichero)
        
 def agregarCarreteras(self):#Para el programa 2
     Programa2.generarInterfaz(self.spinBoxCantCarreteras.value(), self.tableWidgetRutas)

     
 def calCarreteras(self):#Para el programa 2
     Programa2.analizarMatrices(self.spinBoxCantCarreteras.value(), self.tableWidgetRutas, self.comboBoxL.currentText())
     
     
class Programa1():
    def __init__(self):

        pass
    def procesar(rut):

        print(rut)
        wb = load_workbook(filename= rut, read_only=True)
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
        ##------------------ Filtrado Equipos Posibles ------------------##
            
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



        ##------------------ Resolucion de Preguntas ------------------##

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
            
        ## Calcula la septima pregunta
            
        matrizDiferecias= []#Matriz con las diferencias temporada por temporada de cada equipos
        indicesMaximaDif =[]#Indica en que temporadas se dio O dieron las mayores diferencias   
        maximoValorTemp = 0

        for i in range(0,len(equiposValidos)):
            listaDiferenciasEquipo = []
            listaDiferenciasEquipo.append(abs(hoja1Validos[i][8] - hoja2Validos[i][8]))
            listaDiferenciasEquipo.append(abs(hoja2Validos[i][8] - hoja3Validos[i][8]))
            listaDiferenciasEquipo.append(abs(hoja3Validos[i][8] - hoja4Validos[i][8]))
            listaDiferenciasEquipo.append(abs(hoja4Validos[i][8] - hoja5Validos[i][8]))
            matrizDiferecias.append(listaDiferenciasEquipo)
            
        for i in range(0,len(preguntas)):
            maximoValorTemp = max(matrizDiferecias[i])
            preguntas[i][7] = maximoValorTemp 
            listaTempoIndices = []
            for j in range(0, len(matrizDiferecias[i])):
                if maximoValorTemp == matrizDiferecias[i][j]:
                    listaTempoIndices.append(j)
            indicesMaximaDif.append(listaTempoIndices)


        ##Calcula el mayor para la pregunta 1    
        #guardar la lista de los valores
        listaVictorias = []
        maximosVictorias=""
        for i in range(0, len(preguntas)):
            listaVictorias.append(preguntas[i][1])
            
        maximoVic = max(listaVictorias)

        for i in range (0, len(listaVictorias)):
            if (listaVictorias[i] == maximoVic):
                maximosVictorias += " - "  + preguntas[i][0] 

        ##Calcula el mayor para la pregunta 2   
        #guardar la lista de los valores
        listaEmpates = []
        maximosEmpatadores=""
        for i in range(0, len(preguntas)):
            listaEmpates.append(preguntas[i][2])
            
        maximoEmpates = max(listaEmpates)

        for i in range (0, len(listaEmpates)):
            if (listaEmpates[i] == maximoEmpates):
                maximosEmpatadores += " - "  + preguntas[i][0] 

        ##Calcula el mayor para la pregunta 3
        #guardar la lista de los valores
        listaDerrotas = []
        maximosDerrotas=""
        for i in range(0, len(preguntas)):
            listaDerrotas.append(preguntas[i][3])
            
        maximoDerr = max(listaDerrotas)

        for i in range (0, len(listaDerrotas)):
            if (listaDerrotas[i] == maximoDerr):
                maximosDerrotas += " - " + preguntas[i][0]
                
        ##Calcula el mayor para la pregunta 4
        #guardar la lista de los valores
        listaGolesFavor = []
        maximosGolesFavor=""
        for i in range(0, len(preguntas)):
            listaGolesFavor.append(preguntas[i][4])
            
        maximoGF = max(listaGolesFavor)

        for i in range (0, len(listaGolesFavor)):
            if (listaGolesFavor[i] == maximoGF):
                maximosGolesFavor += " - "  + preguntas[i][0]
                
        ##Calcula el mayor para la pregunta 5
        #guardar la lista de los valores
        listaGolesContra = []
        menosGolesContra=""
        for i in range(0, len(preguntas)):
            listaGolesContra.append(preguntas[i][5])
            
        menosGE = min(listaGolesContra)

        for i in range (0, len(listaGolesContra)):
            if (listaGolesContra[i] == menosGE):
                menosGolesContra += " - " + preguntas[i][0]
                
        ##Calcula el mayor para la pregunta 6
        #guardar la lista de los valores
        listaPuntos = []
        maximosPuntos=""
        for i in range(0, len(preguntas)):
            listaPuntos.append(preguntas[i][6])
            
        maximoPuntos = max(listaPuntos)

        for i in range (0, len(listaPuntos)):
            if (listaPuntos[i] == maximoPuntos):
                maximosPuntos += " - " + preguntas[i][0]
                
        ##Calcula el mayor para la pregunta 7
        #guardar la lista de los valores
        listaDifPuntos = []
        maximosDifPuntos=""
        for i in range(0, len(preguntas)):
            listaDifPuntos.append(preguntas[i][7])
            
        maximoDifPuntos = max(listaDifPuntos)

        for i in range (0, len(listaDifPuntos)):
            if (listaDifPuntos[i] == maximoDifPuntos):
                maximosDifPuntos += " - " + preguntas[i][0]

        ##Procedimiento para generar la matriz para ver la temporada de mayor diferencia por equipo
        matrizDatosTemporada = []

        for i in range(0, len(equiposValidos)):
            filaTemp = []
            filaTemp.append(equiposValidos[i])
            filaTemp.append(preguntas[i][7])
            for j in range(0, len (indicesMaximaDif[i])):
                varTemporadaras = ""

                if indicesMaximaDif[i][j] == 0:
                    varTemporadaras += " 2011 - 2012 a 2012 - 2013/ "       
                if indicesMaximaDif[i][j] == 1:
                    varTemporadaras += " 2012 - 2013 a 2013 - 2014/ "
                if indicesMaximaDif[i][j] == 2:
                    varTemporadaras += " 2013 - 2014 a 2014 - 2015/ "
                if indicesMaximaDif[i][j] == 3:
                    varTemporadaras += " 2014 - 2015 a 2015 - 2016/ "
                filaTemp.append(varTemporadaras)
            
            matrizDatosTemporada.append(filaTemp)
            
        ### ------------------------ ESCRIBE EL EXCEL ------------------------###
        #Libro
        wbFinal = Workbook()
        #Worksheet
        wsFinal = wbFinal.active

        # Primera Fila
        wsFinal.append(["Equipos", "Victorias", "Empates", "Derrotas", "GF", "GE", "PTS", "Mayor dif. PTS"])

        #Matriz de resultados
        for i in range(0, len(preguntas)):
            wsFinal.append(preguntas[i])
        wsFinal.append(["", "", ""])
        wsFinal.append(["Categoria", "Equipos", "Total"])
        #                 Categoria/        Nombres Equipos   / Total
        wsFinal.append(["Más Victorias:", maximosVictorias, maximoVic])
        wsFinal.append(["Más Empates:", maximosEmpatadores, maximoEmpates])
        wsFinal.append(["Más Derrotas:", maximosDerrotas, maximoDerr])
        wsFinal.append(["Más Goles a Favor:", maximosGolesFavor, maximoGF])
        wsFinal.append(["Menos Goles en Contra:", menosGolesContra, menosGE])
        wsFinal.append(["Mayor Puntuación:", maximosPuntos, maximoPuntos])

        wsFinal.append(["Mayor Diferencia de Puntos:", maximosDifPuntos, maximoDifPuntos])

        wsFinal.append(["", "", ""])
        wsFinal.append(["Mayor diferencia en temporada"])
        wsFinal.append(["Equipo", "Dif", "Temporada"])

        for i in range(0, len(equiposValidos)):
            wsFinal.append(matrizDatosTemporada[i]) 

        # Guarda el archivo
        wbFinal.save("Resultado.xlsx")

class Programa2():
    def __init__(self):
        pass
    
    def generarInterfaz(val,tableWidgetRutas):##Fija la cantidad de filas segun la cantidad de carreteras
        cantCarreteras = val
        tableWidgetRutas.setRowCount( 0);
        while cantCarreteras != 0:
            rowPosition = tableWidgetRutas.rowCount()
            tableWidgetRutas.insertRow(rowPosition)
            tableWidgetRutas.setItem(rowPosition,0, QtGui.QTableWidgetItem("R" + str(rowPosition + 1)))
            cantCarreteras -= 1
        
        
    def analizarMatrices(val,tableWidgetRutas, formatoLongitud):
        print(formatoLongitud)
        cantFilas = val
        tablacondiciones = []
        #numeroCarreteras = int (input("Digite algo: ")) 
        table = list(product([0, 1], repeat = cantFilas))# 3 por ahora
        
        for i in range(0, cantFilas):
            filaTemp = []
            filaTemp.append(float(tableWidgetRutas.item(i,1).text()))
            filaTemp.append(float(tableWidgetRutas.item(i,2).text()))
            filaTemp.append(float(tableWidgetRutas.item(i,3).text()))
            filaTemp.append(float(tableWidgetRutas.item(i,4).text()))
            tablacondiciones.append(filaTemp)
        print(tablacondiciones)
         
 #       r1 = [22,32.3,4.5,15]
  #      r2 = [62,53,7,122]
   #     r3 = [73.8,68,8,143]
    
    #    tablacondiciones.append(r1)
       # tablacondiciones.append(r2)
      #  tablacondiciones.append(r3)  
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

## MAIN ##
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MyWindow = Principal(None)
    MyWindow.show()
    app.exec_()

