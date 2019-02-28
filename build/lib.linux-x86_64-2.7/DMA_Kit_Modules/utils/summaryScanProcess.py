'''
clase que permite generar el resumen del proceso al momento de generar el clustering exploratorio genera histogramas por las medidas de desempeno
ranking con respecto a las mejores medidas y un resumen estadistico del proceso

'''

import pandas as pd
import numpy as np
from DMA_Kit_Modules.graphic import createCharts

class summaryProcessClusteringScan(object):

    def __init__(self, dataSetFile, pathResponse, performance):

        self.dataSetFile = dataSetFile
        self.dataFrame = pd.read_csv(dataSetFile)
        self.pathResponse = pathResponse
        self.performance = performance

    #metodo que permite hacer los histogramas por las medidas de desempeno
    def createHistogram(self):

        graphic = createCharts.graphicsCreator()

        for key in self.performance:
            print "Create histogram for ", key
            namePicture = self.pathResponse+key+".svg"
            title = "Histogram for "+key
            graphic.generateHistogram(self.dataFrame, key, namePicture, title)

    #metodo que permite crear el resumen estadistico
    def createStatisticSummary(self):

        matrixResponse = []
        header = ["Performance", "Mean", "STD", "Variance", "Min", "Max"]

        #trabajamos con las estadisticas...
        for key in self.performance:
            try:
                print "Process ", key
                row = []
                row.append(key)
                row.append(np.mean(self.dataFrame[key]))
                row.append(np.std(self.dataFrame[key]))
                row.append(np.var(self.dataFrame[key]))
                row.append(min(self.dataFrame[key]))
                row.append(max(self.dataFrame[key]))
                matrixResponse.append(row)
            except:
                pass

        df = pd.DataFrame(matrixResponse, columns=header)
        df.to_csv(self.pathResponse+"summaryStatistical.csv", index=False)

    #metodo que permite poder ordenar los arreglos de mayor a menor segun su valor
    def createRankingFile(self):

        #por cada medida, generamos un ranking con los primeros 10 modelos resultantes
        for data in self.performance:

            rankingPerformance = self.dataFrame.sort_values(data,ascending=False)
            rankingPerformance.to_csv(self.pathResponse+data+"_ranking.csv", index=False)
