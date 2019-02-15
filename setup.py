########################################################################
# setup.py,
#
# Script that allows to generate the installation of the project and the
# python modules in the directory of the same, in order to be able to be
# recognized from any python call and be indexed within the library itself.
#
# Copyright (C) 2019  David Medina Ortiz, david.medina@cebib.cl
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
########################################################################
from distutils.core import setup
import ConfigParser
import os

class SetupConfiguration:

    def __init__(self):

        self.setupInstall()

    def setupInstall(self):

        setup(name='DMA_Kit_Project',
            version='1.0',
            description='DMAKit, is a set of libraries that facilitate the development of data set analysis through the application of data mining techniques, the training of prediction and classification models and the search of patterns, always applying supervised and unsupervised learning algorithms',
            author='David Medina, Diego Inostroza, Lukas Jeldes, Cristofer Quiroz',
            author_email='david.medina@cebib.cl',
            license='Open GPL 3',
            packages=['DMA_Kit_Modules', 'DMA_Kit_Modules.clustering_analysis', 'DMA_Kit_Modules.checks_module', 'DMA_Kit_Modules.feature_analysis', 'DMA_Kit_Modules.statistics_analysis', 'DMA_Kit_Modules.supervised_learning_analysis', 'DMA_Kit_Modules.user_module', 'DMA_Kit_Modules.dataBase_module', 'DMA_Kit_Modules.supervised_learning_predicction', 'DMA_Kit_Modules.utils', 'DMA_Kit_Modules.statistical_test', 'DMA_Kit_Modules.graphic'],)

def main():

    setup = SetupConfiguration()
    return 0

if __name__ == '__main__':
    main()
