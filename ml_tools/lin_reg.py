import pandas as pd
import pymssql
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time as t

x = 0

# connection zu sql datenbank
password = input("Bitte geben Sie das Serverpasswort ein: ")
conn = pymssql.connect("pcs.f4.htw-berlin.de", "Masterprojekt",
                       password, "PraediktiveAnalysenTest")
cursor = conn.cursor()

# letzte 20 werte aus sql datenbank als dataframe lesen
def read_db():
    global df
    df = pd.read_sql('SELECT TOP 20 * FROM Test_Datensatz ORDER BY ID DESC', conn)
    # Zähler zum Dataframe hinzufügen 
    counter = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
    df["Counter"] = counter
    # print(df)

# lineare regression
def lin_reg():
    global df, model, predicted
    model = LinearRegression()
    model.fit(df[["Counter"]], df[["Leistungsaufnahme"]])
    predicted = model.predict([[30], [140]])
    """
    print("-----------------------")
    print("Intercept: " + str(model.intercept_))
    print("Coef: " + str(model.coef_))
    print("-----------------------")
    print("Prediction t + 5 min: " + str(predicted[0]))
    print("Prediction t + 60 min: " + str(predicted[1]))
    print(df)
    """

def rul_predict():
    global df, model
    coef = float(model.coef_[0])
    cur = float(df["Leistungsaufnahme"][0])
    print(cur)
    rul = round((25.0 - cur) / coef * 0.5,2)
    print("-----------------------")
    print("Remaining usefull life: " + str(rul) + " minutes")
    print("-----------------------")
    
"""
# Daten plotten
plt.scatter(df["Counter"], df["Leistungsaufnahme"])
plt.plot([0, 120], predicted, color="red")
plt.show()
"""
y = 30

while x < y:
    read_db()
    lin_reg()
    rul_predict()
    x = x + 1
    t.sleep(5)

print("Ende!")

conn.close()
