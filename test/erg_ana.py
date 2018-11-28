import numpy as np
import pymssql
import matplotlib.pyplot as plt
import pandas as pd

password = "Masterprojekt"
conn = pymssql.connect("pcs.f4.htw-berlin.de",
                       "Masterprojekt", password, "PraediktiveAnalysenTest")
cursor = conn.cursor()

df = pd.read_sql('SELECT * FROM predictions', conn)

plt.scatter(df["Timestamp"], df["Ausfallzeitpunkt"])
# plt.plot([0, 120], predicted, color="red")
plt.show()

conn.close()