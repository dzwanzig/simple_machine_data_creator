import pymssql
# from os import getenv

password = input("Bitte geben Sie das Serverpasswort ein: ")

# new_row = ("","","","","","","","") # Neue Zeile für Serverübergabe
# print("Leere Liste: " + str(new_row))

new_row = ('ABC10050100', '2018-01-18 09:30:01', 100.0, 18.53, 0.092, 75.072, 100.0, 'leer')
print("Gefüllte Liste: " + str(new_row))

# new_row_str = str(new_row)

conn = pymssql.connect("pcs.f4.htw-berlin.de", "Masterprojekt", password, "PraediktiveAnalysenTest")
cursor = conn.cursor()

# cursor.execute('SELECT LEISTUNGSAUFNAHME FROM Test_Datensatz WHERE ID=%s', 'ABC10000215')

# Letzte ID abrufen
cursor.execute('SELECT TOP 1 * FROM Test_Datensatz ORDER BY ID DESC')
list_1 = cursor.fetchall()


"""
cursor.executemany(
    "INSERT INTO Test_Datensatz VALUES (%d, %s, %s, %s, %s, %s, %s, %s)",
    [new_row])

# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()

cursor.execute('SELECT TOP 1 * FROM Test_Datensatz')
list_1 = cursor.fetchall()
"""

print(list_1)
print(type(list_1[0]))

"""
# ID extrahieren
a = list_1[0]
a = a[0]
a = int(a.replace("ABC","")) - 10000000
print(a)

# Uhrzeit extrahieren
b = list_1[0]
b = b[1]
print(b)
print(type(b))
"""

conn.close()