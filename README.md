## README

DMAKit, is an open access library implemented in Python programming language that facilitate the analysis of different kind of data, data mining and pattern recognition techniques, facilitating the implementation of classification, prediction or clustering models, the statistical evaluations and feature analysis of different attributes in dataset.

## Design and implementation

DMAKit was designed under the Object Oriented Programming paradigm, taking advantage of this, the advantages of this paradigm, generating the encapsulation and modularization necessary for this type of development. Its implementation is based on a set of modules written in Python programming language, version 2.7. All modules for generating supervised and unsupervised learning models are based on  scikit-learn library. The data set management is through Pandas library and the graphics using Matplotlib. Finally, scripts have been generated that allow the installation of the modules and be enabled to be imported from any python script, using Disutils to fulfill this objective. Each component was tested using general and public knowledge data sets. The source code and test sets are hosted in the github repository for free access and non-commercial use and license under GNU OpenGL 3.0.

## DMAKit modules

DMAKit is composed of four principal modules, which allow to evaluate characteristics, to develop statistical analysis of the data, to search patterns by means of clustering algorithms and to train classification or regression models through supervised learning algorithms. In addition, it has an exploratory model tool for both types of learning, which allows to evaluate different algorithms and parameters for the same dataset and to evaluate distributions of performance measures associated with the results of the generated models.

## 1. Feature Analysis

The feature analysis module allows the evaluation of relations between  different attributes based on the analysis of the correlation matrix and mutual information techniques. It also implements different dimensionality reduction algorithms, based on linear models, such as Principal Component Analysis (PCA) and its variants, PCA Kernel and Incremental PCA. Additionally, it allows to evaluate the relevance of attributes in the training of supervised learning models using the Random Forest algorithm, both for classification systems and for the  prediction of continuous variables (only available for data sets with response in their features).

For execute Feature analysis module you should exec the script launcherFeatureAnalysis.py, if you wont see all options this script, please exec with option -h:

```
python launcherFeatureAnalysis.py -h
```
