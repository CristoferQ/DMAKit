
import json
import os
from random import uniform

class responseProcess(object):

    #metodo que permite crear un directorio donde se almacene la informacion
    def createDirResult(self, path):

        if path[-1] != "/":
            path = path+"/"

        randomDir = str(uniform(0,10000)).replace(".","")
        nameDir = "%s%s/" % (path, randomDir)
        command = "mkdir -p %s" % nameDir
        os.system(command)

        return nameDir

    #metodo que permite generar un archivo json
    def createJSONFile(self, dictResponse, nameFile):

        with open (nameFile, 'w') as fp:
            json.dump(dictResponse, fp)

    #metodo que permite validar si el data set existe
    def validateDataSetExist(self, dataSet):

        if os.path.isfile(dataSet):
            return 0#exist!
        else:
            return 1#not exist!

    #metodo que permite validar si existe el directorio output
    def validatePath(self, pathData):

        if os.path.exists(pathData):
            return 0#exist!
        else:
            return 1#not exist!
