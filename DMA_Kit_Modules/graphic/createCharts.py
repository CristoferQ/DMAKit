'''
clase con diferentes metodos asociados a la creacion de graficos de diferentes tipos
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class graphicsCreator(object):

    #metodo que permite crear el grafico de torta
    def createPieChart(self, keys, values, namePicture):

        df = pd.DataFrame(values, index=keys, columns=['Groups'])
        # make the plot
        df.plot(kind='pie', subplots=True, figsize=(8, 8))
        plt.savefig(namePicture)

    #metodo que permite crear un grafico de barras
    def createBarChart(self, keys, values, xLabel, yLabel, title, namePicture):

        # Fake dataset
        y_pos = np.arange(len(keys))

        # Create bars and choose color
        plt.bar(y_pos, values, color = (0.5,0.1,0.5,0.6))

        # Add title and axis names
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)

        # Limits for the Y axis
        plt.ylim(0,100)

        # Create names
        plt.xticks(y_pos, keys)

        # Show graphic
        plt.savefig(namePicture)
