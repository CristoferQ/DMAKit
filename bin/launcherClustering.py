'''
script que permite ejecutar el clustering el cual ha sido seleccionado via web, recibe los parametros y genera los resultados pertinentes,
ademas trabaja con formato json para poder generar la lectura desde el javascript en el lado web y hacer la carga de los elementos de una
manera mas sencilla
'''

from DMA_Kit_Modules.clustering_analysis import execAlgorithm
from DMA_Kit_Modules.checks_module import checksParams
from DMA_Kit_Modules.utils import responseResults

import pandas as pd
import sys
import json
import argparse

#dictParams in defaultCase
paramsDefault = ["3", "3", "ward-euclidean-2", "Default", "Default", "Default"]

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to Normalize data set: 1. Normal Scale\n2. Min Max Scaler\n3. Log scale\n4. Log normal scale", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
parser.add_argument("-a", "--algorithm", help="Algorithm to process clustering: 1.K-means\n2.Birch\n3.Agglomerative\n4.DBSCAN\n5.MeanShift\n6.Affinity Propagation", required=True)
parser.add_argument("-i", "--params", help="Params to exec algorithm, pleas add in this form: param1-param2-param3")
args = parser.parse_args()

#hacemos las validaciones asociadas a si existe el directorio y el set de datos
processData = responseResults.responseProcess()#parser y checks...

if (processData.validatePath(args.pathResult) == 0):

    if (processData.validateDataSetExist(args.dataSet) == 0):

        dataSet = args.dataSet
        option = int(args.option)
        pathResult = args.pathResult
        algorithm = int(args.algorithm)

        if algorithm >=1:
            if args.params:
                #instanciamos a checksParams para la revision de los parametros
                checksValues = checksParams.checkParams()
                responseData = checksValues.checkParamsCluster(args.params, algorithm)

                if responseData == "OK":
                    #hacemos la ejecucion
                    if algorithm <4:
                        params = args.params.split("-")
                    else:
                        params = args.params
                    #hacemos la instancia del obeto...

                    execProcess = execAlgorithm.execAlgorithm(pd.read_csv(dataSet), pathResult, algorithm, params, option)
                    execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego
                else:
                    print responseData

            else:
                params = paramsDefault[algorithm-1]

                #hacemos la ejecucion
                if algorithm <4:
                    params = params.split("-")

                #hacemos la instancia del obeto...

                execProcess = execAlgorithm.execAlgorithm(pd.read_csv(dataSet), pathResult, algorithm, params, option)
                execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego
        else:
            print "Please check input data for select algorithm"
    else:
        print "Data set input not exist, please check the input for name file data set"
else:
    print "Path result not exist, please check input for path result"
