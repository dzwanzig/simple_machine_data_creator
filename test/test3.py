import pandas as pd
import pymssql
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#connection zu sql datenbank
conn = pymssql.connect("pcs.f4.htw-berlin.de", "Masterprojekt",
                       "Masterprojekt", "PraediktiveAnalysenTest")
cursor = conn.cursor()

#sql datenbank als dataframe lesen
df = pd.read_sql('SELECT * FROM Test_Datensatz', conn)

#lineare regression
model = LinearRegression()
model.fit(df[["Vibration"]], df[["Temperatur"]])
predicted = model.predict([[0], [0.6]])
print("-----------------------")
print("Intercept: " + str(model.intercept_))
print("Coef: " + str(model.coef_))
print("-----------------------")
print(df)

#ausgleichsgerade
plt.scatter(df["Vibration"], df["Temperatur"])
plt.plot([0, 0.6], predicted, color="red")
plt.show()

#for row in cursor:
# print('row = %r' % (row,))

conn.close()
