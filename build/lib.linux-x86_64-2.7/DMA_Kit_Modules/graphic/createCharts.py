
'''
clase con diferentes metodos asociados a la creacion de graficos de diferentes tipos
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

    #metodo que permite crear un grafico de barras dobles comparativas
    def createBarChartCompare(self, values1, values2, label1, label2, xLabel, yLabel, listData, namePicture):
        plt.figure()
        listData = list(set(listData))
        # set width of bar
        barWidth = 0.25

        # Set position of bar on X axis
        r1 = np.arange(len(values1))
        r2 = [x + barWidth for x in r1]

        # Make the plot
        plt.bar(r1, values1, color='#7f6d5f', width=barWidth, edgecolor='white', label=label1)
        plt.bar(r2, values2, color='#557f2d', width=barWidth, edgecolor='white', label=label2)

        # Add xticks on the middle of the group bars
        plt.xlabel(xLabel, fontweight='bold')
        plt.ylabel(yLabel, fontweight='bold')

        plt.xticks([r + barWidth for r in range(len(values1))], listData)

        # Create legend & Show graphic
        plt.legend()
        plt.savefig(namePicture)


    #metodo que permite crear el grafico de la matriz de confusion asociada al proceso de entrenamiento de modelos
    def createConfusionMatrixPictures(self, matrixData, listData, namePicture):

        uniqueList = list(set(listData))

        #trabajamos con la data
        dataFrame = pd.DataFrame(matrixData, index=uniqueList, columns=uniqueList)
        #generamos la imagen
        plt.figure()
        heatmap = sns.heatmap(dataFrame)

        loc, labels = plt.xticks()
        heatmap.set_xticklabels(labels)
        heatmap.set_yticklabels(labels[::-1])

        # Add xticks on the middle of the group bars
        plt.xlabel("Prediction Values", fontweight='bold')
        plt.ylabel("Reality Values", fontweight='bold')
        plt.title("Confusion Matrix for training model")

        plt.savefig(namePicture)

    #metodo que permite crearel grafico de scatter plot
    def createScatterPlotErrorPrediction(self, real_values, predict_values, namePicture):

        df=pd.DataFrame({'x': real_values, 'y': predict_values})

        # plot with matplotlib
        plt.plot( 'x', 'y', data=df, marker='o', linestyle='none', color='mediumvioletred')
        plt.xlabel("Real Values", fontweight='bold')
        plt.ylabel("Predict Values", fontweight='bold')
        plt.title("Scatter Plot Real v/s Predict Values")
        plt.savefig(namePicture)
