'''
clase con diferentes metodos asociados a la creacion de graficos de diferentes tipos
'''

import pandas as pd
import matplotlib.pyplot as plt

class graphicsCreator(object):

    #metodo que permite crear el grafico de torta
    def createPieChart(self, keys, values, namePicture):

        df = pd.DataFrame(values, index=keys, columns=['Groups'])
        # make the plot
        df.plot(kind='pie', subplots=True, figsize=(8, 8))
        plt.savefig(namePicture)
