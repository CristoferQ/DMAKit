'''
script que permite generar la ejecucion de un algorithm de aprendizaje supervisado, contemplando la data que es recolectada desde el navegador
ejecuta el proceso y genera los resultados correspondientes con respecto a la data de interes:

matriz de confusion
curva de aprendizaje
curva precision v/s recall
curva roc
summary process con los resultados de las performance obtenidas
'''

from DMA_Kit_Modules.supervised_learning_analysis import execAlgorithm
from DMA_Kit_Modules.utils import responseResults

import pandas as pd
import sys
import argparse

paramsDefault = ["50-SAMME.R", "100-True", "DEFAULT", "gini-best", "DEFAULT","100-deviance-2-1", "5-auto-minkowski-uniform", "relu-adam-constant-1-1-1-0.0001-200-True", "rbf-0.1-3-0.01", "10-gini-2-1-True", "rbf-1-3-0.01"]

#declaracion de los argumentos de entrada
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to Normalize data set: 1. Normal Scale\n2. Min Max Scaler\n3. Log scale\n4. Log normal scale", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)
parser.add_argument("-r", "--responseClass", help="Name of attribute with response class", required=True)
parser.add_argument("-a", "--algorithm", help="Algorithm to process training model: 1. AdaBoostClassifier 2. BaggingClassifier 3. BernoulliNB 4. DecisionTree 5. GaussianNB 6. GradientBoostingClassifier 7. KNeighborsClassifier 8. MLPClassifier 9. NuSVC 10. RandomForest 11. SVC (Default SVC)", required=True)
parser.add_argument("-v", "--validation", help="Cross validation value. If you wont use a Leave One Out, input -1", required=True)
parser.add_argument("-i", "--params", help="Params to exec algorithm, pleas add in this form: param1-param2-param3 for more detail, checks de user manual. If you add Default, it will user the Default params", default="DEFAULT")
args = parser.parse_args()

processData = responseResults.responseProcess()#parser y checks...

if (processData.validatePath(args.pathResult) == 0):

    if (processData.validateDataSetExist(args.dataSet) == 0):

        dataSet = pd.read_csv(args.dataSet)
        option = args.option
        pathResult = args.pathResult
        algorithm = int(args.algorithm)
        validation = int(args.validation)
        featureClass = args.responseClass
        params = args.params

        if params == "DEFAULT":
            if algorithm>11 or algorithm<=0:
                algorithm=11
            paramsValues = paramsDefault[algorithm-1]
            paramsValues = paramsValues.split("-")
            print paramsValues
            #hacemos la instancia del obeto...
            execProcess = execAlgorithm.execAlgorithm(dataSet, pathResult, algorithm, paramsValues, validation, featureClass, option)
            execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego
        else:
            paramsValues = params.split("-")
            print paramsValues
            #hacemos la instancia del obeto...
            execProcess = execAlgorithm.execAlgorithm(dataSet, pathResult, algorithm, paramsValues, validation, featureClass, option)
            execProcess.execAlgorithmByOptions()#hacemos la ejecucion del algoritmo con respecto a la data que se entrego
    else:
        print "Data set input not exist, please check the input for name file data set"
else:
    print "Path result not exist, please check input for path result"
