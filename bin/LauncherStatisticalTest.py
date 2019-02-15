'''
launcher asociado al proceso de test estadisticos, es capaz de representar diferentes test con respecto a la opcion a desarrollar
'''

import sys
import json
import argparse
from DMA_Kit_Modules.statistical_test import launcherStatisticalTest
from DMA_Kit_Modules.utils import responseResults

#instanciamos a argparse para recibir la informacion correspondiente
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataSet", help="full path and name to acces dataSet input process", required=True)
parser.add_argument("-o", "--option", type=int, help="Option to process statistical analysis: 1:Pearson\n2:Spearman\n3:Kendalltau\n4:MannWhitney\n5:Kolmogorov\n6:Shapiro-Wilk\n7:T-Test", required=True)
parser.add_argument("-p", "--pathResult", help="full path for save results", required=True)

args = parser.parse_args()

processData = responseResults.responseProcess()#parser y checks...
#recibimos la data de interes...
dataSet = args.dataSet
optionProcess = args.option
pathResult = args.pathResult

#verificamos si el set de datos existe
if processData.validateDataSetExist(dataSet) == 0:
    if processData.validatePath(pathResult) == 0:
        print "Process statistical test"

        #hacemos la instancia al objeto y ejecutamos el proceso
        launcherProcess = launcherStatisticalTest.statisticalTest(dataSet, optionProcess)
        launcherProcess.checkExec()

        nameFile = "%sstatistical_test_result.json" % pathResult
        processData.createJSONFile(launcherProcess.response, nameFile)

        print "Finish process option and Job"
    else:
        print "Path result not exist, please check input for path result"
else:
    print "Data set input not exist, please check the input for name file data set"
