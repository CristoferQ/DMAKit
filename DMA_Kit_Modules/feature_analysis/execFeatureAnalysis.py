'''
clase que recibe una solicitud y genera la instancia con respecto al tipo de
respuesta que se espera, procesa todas las opciones segun lo que solicita el usuario
desde la opcion web. Evalua si el data set tiene clases o corresponde a algun tipo clustering o prediccion de elementos
'''

from DMA_Kit_Modules.dataBase_module import ConnectDataBase
from DMA_Kit_Modules.dataBase_module import HandlerQuery
from DMA_Kit_Modules.feature_analysis import correlationValue
from DMA_Kit_Modules.feature_analysis import spatialDeformation
from DMA_Kit_Modules.feature_analysis import kernelPCA
from DMA_Kit_Modules.feature_analysis import mutualInformation
from DMA_Kit_Modules.feature_analysis import PCA_Method

class featureAnalysis(object):

    def __init__(self, dataSet, pathResponse):

        self.dataSet = dataSet
        self.pathResponse = pathResponse

    #metodo que permite la ejecucion de la correlacion de datos
    def execCorrelationData(self, optionNormalize):

        corrObject = correlationValue.correlationMatrixData(self.dataSet, self.pathResponse, optionNormalize)
        return corrObject.calculateCorrelationMatrix()

    #metodo que permite la ejecucion de la deformacion de espacio con random forest
    def excecSpatialDeformation(self, feature, kindDataSet, optionNormalize):
        spatial = spatialDeformation.spatialDeformation(self.dataSet, self.pathResponse, optionNormalize)
        return spatial.applySpatialDeformation(feature, kindDataSet)

    #metodo que permite la ejecucion de mutual information...
    def execMutualInformation(self, optionNormalize):

        mutualObject = mutualInformation.mutualInformation(self.dataSet, self.pathResponse, optionNormalize)
        return mutualObject.makeMatrix()

    #metodo que permite la ejecucion de PCA information...
    def execPCA(self, optionNormalize):

        pcaObject = PCA_Method.pca(self.dataSet, self.pathResponse, optionNormalize)
        return pcaObject.doPCA()

    #metodo que permite la ejecucion de incremental PCA...
    def execPCA_Incremental(self, optionNormalize):

        pcaObject = PCA_Method.pca(self.dataSet, self.pathResponse, optionNormalize)
        return pcaObject.incrementalPCA()

    #metodo que permite la ejecucion de kernel pca...
    def exec_kernelPCA(self, optionNormalize):

        kernelObject = kernelPCA.kpca(self.dataSet, self.pathResponse, optionNormalize)
        return kernelObject.doKPCA()
