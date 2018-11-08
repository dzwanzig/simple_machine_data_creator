# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:30:04 2018

@author: bassmaniac
"""


# Einladen CSV-Datei
# Grafische Darstellung Punktdiagramm
# Ausgabe Regressionswerte

import statsmodels.api as sm  # laden statistikmodul

import matplotlib.pyplot as plt  # Bibliothek zur Datenvisualisierung
import pandas as pd  # Aufrufen der Pandas Bibliothek (Daten Analyse Tools)
import numpy as np  # Aufrufen numerisches Python (Matrizen, lineare Algebra)

# Import der Trennungsfunktion in Test-Daten aus bestehenden Daten
from sklearn.model_selection import train_test_split
# Einladen der Skalierungsfunktion für Anpassung Matrix[-1,1]
from sklearn.preprocessing import StandardScaler
# importieren der linearen Regression aus sklearn
from sklearn.linear_model import LinearRegression


# Namensgebung und Aufruf der CSV-Datei
data = pd.read_excel("dummy3.xlsx", "Set2",
                     usecols=[1, 3], index_col=0)

data.head()  # Ausgabe der Daten in Console
data.info()  # Ausgabe von Informationen über geladene Daten

# Punktdiagramm
data.plot(y='Leistungsaufnahme')

# Zuweisung Variablen zu Spalten im Datensatz
X = data.index
y = data['Leistungsaufnahme']

# Notwendig, um Matrix für X (Groesse) in Werte -1,1 zu ändern, da sonst Fehler
sc_X = StandardScaler()
X = np.array(X).reshape(-1, 1)
X = sc_X.fit_transform(X)

model = sm.OLS(y, X).fit()
predictions = model.predict(X)  # make the predictions by the model

# Anzeige der Regressionswerte/ des Modells
model.summary()

# Zuordnung der Testdaten aus bestehendem Datensatz
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,     # 70% der Daten für das Training
                                                    random_state=None)  # bei Bedarf kann hier "dem Zufall auf die Sprünge geholfe


# Benennung der Klasse (Instanzierung)
lr = LinearRegression()
# trainieren der Funktion
lr.fit(X_train, y_train)


# Ausdruck der Werte
print('------ Lineare Regression -----')
print('Funktion via sklearn: y = %.3f * x + %.3f' %
      (lr.coef_[0], lr.intercept_))
print("Alpha: {}".format(lr.intercept_))
print("Beta: {}".format(lr.coef_[0]))
print("Training Set R² Score: {:.2f}".format(lr.score(X_train, y_train)))
print("Test Set R² Score: {:.2f}".format(lr.score(X_test, y_test)))
print("\n")


# Ausdruck des Regressionsplots
plt.figure(figsize=(10, 10))
# Blaue Punkte sind Trainingsdaten
plt.scatter(X_train, y_train, color='blue')
# Grüne Punkte sind Testdaten
plt.scatter(X_test, y_test, color='green')
# Hier ensteht die Gerade (x, y) = (x, lr.predict(x)
plt.plot(X_train, lr.predict(X_train), color='red')
# plt.xlabel(X_train[0])
# plt.ylabel(y[0])
plt.show()

intercept = (lr.intercept_)
slope = (lr.coef_)
