# -*- coding: utf-8 -*-
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import autocorrelation_plot
"""
Created on Mon Nov  5 14:09:39 2018

@author: bassmaniac
"""


import matplotlib.pyplot as plt  # Bibliothek zur Datenvisualisierung
import pandas as pd  # Aufrufen der Pandas Bibliothek (Daten Analyse Tools)
import numpy as np  # Aufrufen numerisches Python (Matrizen, lineare Algebra)
import os
from pandas import DataFrame
from pandas import read_csv
from pandas import datetime


# Namensgebung und Aufruf der CSV-Datei
# Aufruf des Sheets Set1, Aufruf der Spalten, erste Spalte "0"
# Zuweisung der Uhrzeit als Index über index_col


dataSet1 = pd.read_excel("dummy3.xlsx", "Set1",
                         usecols=[1, 3], index_col=0)

dataSet2 = pd.read_excel("dummy3.xlsx", "Set2",
                         usecols=[1, 3], index_col=0)

"""
# GUI zur Anzeige, funktioniert zum Teil
import tkinter as tk

from tkinter import *

 
master = Tk()
 
def callback():
    plt.figure(1)             # Make the first figure
    plt.clf()
    plt.subplot(2, 1, 1)  # 2 rows, 1 column, plot 1
    plt.plot(dataSet1)
    plt.title('dataSet1')
    plt.text(2, 0.8, 'dataSet1')

    plt.subplot(2, 1, 2)  # 2 rows, 1 column, plot 2
    plt.plot(dataSet2)
    plt.title('dataSet2')
    plt.text(2, 0.8, 'dataSet2')
    print ("Set1 anzeigen")
 
b = Button(master, text="Set1 anzeigen", command=callback)
b.pack()
 
mainloop()
"""

""" Alternative Zuweisung
# Zuweisung der Uhrzeit als Index
data.index = pd.read_excel("dummy3.xlsx", "Set1",
                     usecols=[1])
"""

# Ausgabe der Daten in Console
print("Data Head")
print(dataSet1.head(5))
# Ausgabe von Informationen über geladene Daten
print("Data Info")
print(dataSet1.info())


print("Data Head")
print(dataSet2.head(5))
# Ausgabe von Informationen über geladene Daten
print("Data Info")
print(dataSet2.info())


plt.figure(1)             # Make the first figure
plt.clf()
plt.subplot(2, 1, 1)  # 2 rows, 1 column, plot 1
plt.plot(dataSet1)
plt.title('dataSet1')
plt.text(2, 0.8, 'dataSet1')

plt.subplot(2, 1, 2)  # 2 rows, 1 column, plot 2
plt.plot(dataSet2)
plt.title('dataSet2')
plt.text(2, 0.8, 'dataSet2')

""" LagPlot zur optischen Identifizierung der Autokorrelation
from pandas.tools.plotting import lag_plot
lag_plot(dataSet1) 
lag_plot(dataSet2) 
"""


# Aufruf Bibliothek Autokorrelation und Ausdruck

# Plotten der Autokorrelationsfunktionen
plt.figure(2)
autocorrelation_plot(dataSet1)
plt.show()

plt.figure(3)
autocorrelation_plot(dataSet2)
plt.show()

# Import der ARIMA Funtion

# Anpassung des ARIMA-Modells; Order aus Beispiel übernommen
"""First, we fit an ARIMA(5,1,0) model. 
This sets the lag value to 5 for autoregression, 
uses a difference order of 1 to make the time series stationary, 
and uses a moving average model of 0"""

model = ARIMA(dataSet1, order=(10, 1, 0))
model_fit = model.fit(disp=0)
print(model_fit.summary())


# folgendes Skript funktioniert noch nicht: 05.11.2018, 20Uhr
# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot(title='Residuals')
pyplot.show()
residuals.plot(title='Residuals Density', kind='kde')
pyplot.show()
print(residuals.describe())

# Autoregressive Integrated Moving Average (ARIMA)
