'''
scrip que permite ejecutar un algoritmo de clustering, recibe los parametros y estima los valores que son necesarios,
recibe el archivo csv y genera los archivos asociados a los resultados para la generacion de graficos y creacion del csv
con las etiquetas generadas por el algoritmo de clustering.

# NOTE: El archivo con los resultados se encontrara en formato json y contendra el error si es que existe o los valores de
los resultados obtenidos....

# NOTE: Explicacion del atributo param

Param es una lista de parametros dependiente de cada algoritmo, toma los siguientes valores posibles

Algoritmo   Valor param
K_means     k
Birch       k
Aglomerativo [linkage, affinity, numberK]
Otros       Void
'''

from DMA_Kit_Modules.clustering_analysis import processClustering
from DMA_Kit_Modules.clustering_analysis import evaluationClustering
from DMA_Kit_Modules.graphic import createCharts

from DMA_Kit_Modules.utils import transformFrequence
from DMA_Kit_Modules.utils import ScaleNormalScore
from DMA_Kit_Modules.utils import ScaleMinMax
from DMA_Kit_Modules.utils import ScaleDataSetLog
from DMA_Kit_Modules.utils import ScaleLogNormalScore

import pandas as pd
import json

class execAlgorithm(object):

    #constructor de la clase
    def __init__(self, dataSet, pathResponse, algorithm, params, optionNormalize):

        self.optionNormalize = optionNormalize
        self.processDataSet(dataSet)#hacemos el preprocesamiento a los datos

        if pathResponse[-1] == "/":
            self.pathResponse = pathResponse
        else:
            self.pathResponse= pathResponse+"/"

        self.algorithm = algorithm
        self.params = params#params es una lista de parametros asociados al algoritmo
        self.applyClustering = processClustering.aplicateClustering(self.dataSet)
        self.response = {}#diccionario con la respuesta para formar el json

    #metodo que permite procesar el set de datos segun la opcion del usuario a normalizar
    def processDataSet(self, dataSetInput):

        #ahora transformamos el set de datos por si existen elementos discretos...
        transformDataSet = transformFrequence.frequenceData(dataSetInput)
        dataSetNewFreq = transformDataSet.dataTransform

        #ahora aplicamos el procesamiento segun lo expuesto
        if self.optionNormalize == 1:#normal scale
            applyNormal = ScaleNormalScore.applyNormalScale(dataSetNewFreq)
            self.dataSet = applyNormal.dataTransform

        if self.optionNormalize == 2:#min max scaler
            applyMinMax = ScaleMinMax.applyMinMaxScaler(dataSetNewFreq)
            self.dataSet = applyMinMax.dataTransform

        if self.optionNormalize == 3:#log scale
            applyLog = ScaleDataSetLog.applyLogScale(dataSetNewFreq)
            self.dataSet = applyLog.dataTransform

        if self.optionNormalize == 4:#log normal scale
            applyLogNormal = ScaleLogNormalScore.applyLogNormalScale(dataSetNewFreq)
            self.dataSet = applyLogNormal.dataTransform

    #metodo que permite evaluar la ejecucion del algoritmo con respecto a los parametros de entrada
    def execAlgorithmByOptions(self):

        nameDoc = ""
        if self.algorithm == 1:#kmeans

            responseExec = self.applyClustering.aplicateKMeans(int(self.params[0]))

            self.response.update({"algorithm": "K Means"})
            paramsData = {}
            paramsData.update({"Number K": self.params[0]})
            self.response.update({"Params": paramsData})

            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        elif self.algorithm == 2:#Birch

            responseExec = self.applyClustering.aplicateBirch(int(self.params[0]))
            self.response.update({"algorithm": "Birch"})
            paramsData = {}
            paramsData.update({"Number K": self.params[0]})
            self.response.update({"Params": paramsData})

            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        elif self.algorithm == 3:#Agglomerative


            responseExec = self.applyClustering.aplicateAlgomerativeClustering(self.params[0], self.params[1], int(self.params[2]))
            self.response.update({"algorithm": "Agglomerative Clustering"})
            paramsData = {}
            paramsData.update({"Linkage": self.params[0]})
            paramsData.update({"Affinity": self.params[1]})
            paramsData.update({"Number K": self.params[2]})
            self.response.update({"Params": paramsData})

            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        elif self.algorithm == 4:#DBSCAN

            responseExec = self.applyClustering.aplicateDBSCAN()
            self.response.update({"algorithm": "DBSCAN"})
            paramsData = {}
            paramsData.update({"Default": "Default"})
            self.response.update({"Params": paramsData})

            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        elif self.algorithm == 5:#MeanShift

            responseExec = self.applyClustering.aplicateMeanShift()
            self.response.update({"algorithm": "Mean Shift"})
            paramsData = {}
            paramsData.update({"Default": "Default"})
            self.response.update({"Params": paramsData})
            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        else:
            responseExec = self.applyClustering.aplicateAffinityPropagation()
            self.response.update({"algorithm": "Affinity Propagation"})
            paramsData = {}
            paramsData.update({"Default": "Default"})
            self.response.update({"Params": paramsData})
            if responseExec == 0:
                self.response.update({"responseExec":"OK"})
            else:
                self.response.update({"responseExec":"ERROR"})

        #solo si la ejecucion fue correcta!
        if self.response['responseExec'] == "OK":

            print "Eval clustering"
            #evaluamos el clustering y obtenemos los resultados...
            result = evaluationClustering.evaluationClustering(self.dataSet, self.applyClustering.labels)#evaluamos...
            self.response.update({"calinski_harabaz_score": result.calinski})
            self.response.update({"silhouette_score": result.siluetas})

            #print self.response
            #finalmente, agregamos los labels al set de datos y generamos el resultado en el path entregado...
            self.dataSet["Labels"] = pd.Series(self.applyClustering.labels, index=self.dataSet.index)
            self.dataSet.to_csv(self.pathResponse+"responseClustering.csv")

            print "Create file responseClustering.csv"
            #hacemos el conteo de los elementos por grupo para la generacion del grafico de torta asociada a la cantidad de grupos...
            countGroup, keys, values = self.countMemberGroup()
            self.response.update({"membersGroup":countGroup})

            #hacemos la instancia para generar el grafico
            namePic = self.pathResponse+"distributionGroup.png"
            createChartsObject = createCharts.graphicsCreator()
            createChartsObject.createPieChart(keys, values, namePic)

        print self.response
        #exportamos tambien el resultado del json
        with open(self.pathResponse+"responseClustering.json", 'w') as fp:
            json.dump(self.response, fp)

        print "Create file responseClustering.json"

    #metodo que recibe una lista y genera un diccionario asociado a los grupos y su cantidad...
    def countMemberGroup(self):

        keys = []
        values = []

        groups = list(set(self.applyClustering.labels))

        countGroup = {}

        for element in groups:
            cont =0

            for label in self.applyClustering.labels:
                if element == label:
                    cont+=1
            key = "Group"+str(element)
            keys.append(key)
            values.append(cont)
            countGroup.update({key: cont})
        return countGroup, keys, values
