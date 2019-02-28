'''
clase que permite generar el resumen del proceso al momento de generar el clustering exploratorio genera histogramas por las medidas de desempeno
ranking con respecto a las mejores medidas y un resumen estadistico del proceso

'''

import pandas as pd
import numpy as np
from DMA_Kit_Modules.graphic import createCharts

class summaryProcessClusteringScan(object):

    def __init__(self, dataFrame, dataSetFile, pathResponse):

        self.dataSetFile = dataSetFile
        self.dataFrame = dataFrame
        self.pathResponse = pathResponse

    #metodo que permite hacer los histogramas por las medidas de desempeno
    def createHistogram(self):

        keys = ['calinski_harabaz_score', 'silhouette_score', 'groups']

        graphic = createCharts.graphicsCreator()

        for key in keys:
            print "Create histogram for ", key
            namePicture = self.pathResponse+key+".svg"
            title = "Histogram for "+key
            graphic.generateHistogram(self.dataFrame, key, namePicture, title)

    #metodo que permite crear el resumen estadistico
    def createStatisticSummary(self):

        matrixResponse = []
        header = ["Performance", "Mean", "STD", "Variance", "Min", "Max"]

        #trabajamos con las estadisticas...
        for key in self.dataFrame:
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
        rankingCalinkski = self.dataFrame.sort_values('calinski_harabaz_score',ascending=False)
        rankingSiluetas = self.dataFrame.sort_values('silhouette_score',ascending=False)

        rankingCalinkski.to_csv(self.pathResponse+"calinski_harabaz_score_ranking.csv", index=False)
        rankingSiluetas.to_csv(self.pathResponse+"silhouette_score_ranking.csv", index=False)
