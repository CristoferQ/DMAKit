'''
script que permite poder ejecutar las diversas operaciones asociadas a los procesos de analisis estadisticos
que son requeridos durante la ejecucion del proceso...

En general, el proceso consta de:

1. Recuperar la opcion
2. Obtener las caracteristicas y sus tipos
3. Aplicar el proceso segun el tipo que corresponda
4. Generar los archivos de salida
5. Cambiar status de job con respecto a la ejecucion del proceso

'''
from DMA_Kit_Modules.statistics_analysis import processStatiticsSummary
from DMA_Kit_Modules.graphic import createCharts

import json
import pandas as pd
import numpy as np

#definicion de la clase
class launcherStatisticalProcess(object):

    def __init__(self, dataSet, pathResponse, optionProcess, keyFeature):

        self.dataSet = dataSet
        self.pathResponse = pathResponse
        self.optionProcess = int(optionProcess)#el metodo a ejecutar...
        self.keyFeature = keyFeature#key del data set, solo en los casos que corresponde

    #metodo que permite evaluar la opcion a ejecutar...
    def checkExec(self):

        if self.optionProcess == 1:#show data continue

            try:
                graphic = createCharts.graphicsCreator()
                namePicture = self.pathResponse+"viewContinueValuesFor_"+self.keyFeature+".png"
                graphic.createScatterContinueData(self.dataSet[self.keyFeature], namePicture, self.keyFeature)
                print "Create graphic OK"
            except:
                print "Error during create graphic"
                pass

        elif self.optionProcess == 2:#boxplot and violinplot

            try:
                graphic = createCharts.graphicsCreator()
                namePicture = self.pathResponse+"boxplot.svg"
                graphic.createBoxPlot(self.dataSet, namePicture)
                print "Box plot graphic OK"
            except:
                print "Error during create BoxPlot"
                pass

            try:
                graphic = createCharts.graphicsCreator()
                namePicture = self.pathResponse+"violinplot.svg"
                graphic.createViolinPlot(self.dataSet, namePicture)
                print "Violin plot graphic OK"
            except:
                print "Error during create Violin"
                pass
                
        elif self.optionProcess == 3:#histograma

            try:
                graphic = createCharts.graphicsCreator()
                namePicture = self.pathResponse+"histogram_"+self.keyFeature+".svg"
                title = "Histogram for feature "+self.keyFeature
                graphic.generateHistogram(self.dataSet, self.keyFeature, namePicture, title)
                print "create histogram for feature: ", self.keyFeature
            except:
                print "Error during create Histogram"
                pass

        elif self.optionProcess == 4:#frequence

            try:
                keys = list(set(self.dataSet[self.keyFeature]))
                values = []
                for key in keys:
                    cont=0
                    for i in range(len(self.dataSet[self.keyFeature])):
                        if self.dataSet[self.keyFeature][i] == key:
                            cont+=1
                    values.append(cont)
                namePicture = self.pathResponse+"piechartFor_"+self.keyFeature+".svg"
                graphic = createCharts.graphicsCreator()
                graphic.createPieChart(keys, values, namePicture)
                print "Create pie chart for "+self.keyFeature
            except:
                print "Error during create a pie chart"
                pass

        elif self.optionProcess == 5:#parallel
            try:
                graphic = createCharts.graphicsCreator()
                namePicture = self.pathResponse+"parallel_coordinates_"+self.keyFeature+".svg"
                title = "parallel_coordinates for "+self.keyFeature
                graphic.createParallelCoordinates(self.dataSet, self.keyFeature, namePicture, title)
                print "Create parallel_coordinates graphic"
            except:
                print "Error during create a parallel_coordinates"
                pass

        elif self.optionProcess == 6:#SPLOM

            try:
                graphic = createCharts.graphicsCreator()
                namePicture = self.pathResponse+"splom.svg"
                graphic.createScatterPlotMatrix(self.dataSet, namePicture, self.keyFeature)
                print "Create SPLOM for feature ", self.keyFeature
            except:
                print "Error during create SPLOM"
                pass

        else:

            matrixResponse = []
            header = ["Feature", "Mean", "STD", "Variance", "Min", "Max"]

            #trabajamos con las estadisticas...
            for key in self.dataSet:
                try:
                    print "Process ", key
                    row = []
                    row.append(key)
                    row.append(np.mean(self.dataSet[key]))
                    row.append(np.std(self.dataSet[key]))
                    row.append(np.var(self.dataSet[key]))
                    row.append(min(self.dataSet[key]))
                    row.append(max(self.dataSet[key]))
                    matrixResponse.append(row)
                except:
                    pass

            df = pd.DataFrame(matrixResponse, columns=header)
            df.to_csv(self.pathResponse+"summaryStatistical.csv", index=False)

            print "Create summaryStatistical.csv file"
