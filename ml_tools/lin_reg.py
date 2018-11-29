import pandas as pd
import pymssql
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import time as t
from datetime import datetime, timedelta

x = 0

# connection zu sql datenbank
password = input("Bitte geben Sie das Serverpasswort ein: ")
conn = pymssql.connect("pcs.f4.htw-berlin.de", "Masterprojekt",
                       password, "PraediktiveAnalysenTest")
cursor = conn.cursor()

# letzte 20 werte aus sql datenbank als dataframe lesen


def read_db():
    global df, time
    """ This function connects to machine data table in the prediction database an reads the last 20 rows.
    It creates a dataframe with an index from 1 to 20 in the variable 'df' as a pandas data frame and 
    stores the latest timestamp in the variable 'time'. """
    df = pd.read_sql(
        'SELECT TOP 20 * FROM Maschinendaten_20181122 ORDER BY ID DESC', conn)
    last_timestamp = df['Timestamp']
    time = last_timestamp[0]
    print("Last timestamp: " + str(time))
    # adding the counter
    counter = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8,
               7, 6, 5, 4, 3, 2, 1]
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
    global df, model, rul
    coef = float(model.coef_[0])
    cur = float(df["Leistungsaufnahme"][0])
    print(cur)
    rul = round((25.0 - cur) / coef * 0.5 * 60, 0)
    print("-----------------------")
    print("Remaining usefull life: " + str(rul) + " seconds")
    print("-----------------------")

# write data to prediction table


def rul_write():
    """ rul_write stores the predicted useful life in the prediction table in the prediction database. """
    global rul, time, cursor
    id_old = pd.read_sql(
        'SELECT TOP 1 ID FROM predictions ORDER BY ID DESC', conn)
    id_new = id_old['ID']
    id_new = id_new[0] + 1
    rul_time = time + timedelta(seconds=rul)
    print(rul_time)
    new_row = tuple((str(id_new), str(time), "lin_reg", "XL_400_1", str(
        rul_time), "F001", "5"))  # all elements in tuple have to be strings
    sql = "INSERT INTO Predictions VALUES (%d, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, new_row)
    conn.commit()
    print("new_row added")


"""
# Daten plotten
plt.scatter(df["Counter"], df["Leistungsaufnahme"])
plt.plot([0, 120], predicted, color="red")
plt.show()
"""
y = 100

while x < y:
    global rul
    read_db()
    lin_reg()
    rul_predict()
    # call function rul_write() if rull is between 600 and 0
    if 1200 > rul > 0:
        rul_write()
    x += 1
    t.sleep(5)

conn.close()
print("Ende!")
