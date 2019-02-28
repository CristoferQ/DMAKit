'''
script que permite ejecutar el servicio de clustering,
input:
    dataSet
    job
    user
    pathResponse
response:
    csv error process
    csv result process
    histogram calinski
    histogram siluetas
'''

from DMA_Kit_Modules.clustering_analysis import callService

import sys
import pandas as pd

#recibimos los datos de entrada...
dataSet = pd.read_csv(sys.argv[1])
pathResponse = sys.argv[2]
optionNormalize = int(sys.argv[3])

#instancia al objeto
callServiceObject = callService.serviceClustering(dataSet, pathResponse, optionNormalize)
callServiceObject.execProcess()
