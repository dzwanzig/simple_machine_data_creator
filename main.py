# machine data creation tool for machine learning project
# dorian zwanzig 2018-10-27 17:35
# version 0.1.1810271735

import numpy as np
import sys
import random
import time

# Zugriffsversuch auf Ausgabedatei
try: 
    d  = open("output.txt","w")
except:
        print("Zugriff nicht erfolgt")
        sys.exit(0)

# Kopfzeile schreiben
d.write("ID;Drehzahl;Leistungsaufnahme;Vibration;Lautstaerke\n")

# Standardwerte:
std_dz = 100        # Standarddrehzahl
std_la = 18.5       # Standardleistungsaufnahme
std_vb = 0          # Standardvibration
std_ls = 75         # Standardlautstärke
data_id_nr = 1000   # Startwert für die ID Erstellung

# Startzeile setzen
zeile = 1

# Nutzerabfrage: Menge Datensätze
menge = int(input("Bitte Anzahl der gewünschten Datensätze eingeben: ")) + zeile

# Erstellung mehrerer Datensätze durch Schleife (Normalbetrieb)
def normalbetrieb(zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr):
    x = 0
    y = random.randrange(1, 200)
    while x < y:
        drehzahl = std_dz
        leistungsaufnahme = round(np.random.normal(std_la, 0.1),3)
        vibration = round(np.random.normal(std_vb, 0.1),3)
        lautstaerke = round(np.random.normal(std_ls, 0.1),3)
        data_id_nr = 10000000 + zeile
        d.write("ABC" + str(data_id_nr) + ";" + str(drehzahl) + ";" + str(leistungsaufnahme)  + ";" + str(vibration)  + ";" + str(lautstaerke) + "\n")
        zeile = zeile + 1
        x = x + 1
    # print("Normalbetrieb")
    return zeile

# Erstellung mehrerer Datensätze durch Schleife (Wartung)
def wartung(zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr):
    x = 0
    y = random.randrange(1, 50)
    while x < y:
        drehzahl = 0
        leistungsaufnahme = round(np.random.normal(std_la*0.1, 0.1),3)
        vibration = round(np.random.normal(std_vb*2, 0.1),3)
        lautstaerke = round(np.random.normal(std_ls*0.3, 0.1),3)
        data_id_nr = 10000000 + zeile
        d.write("ABC" + str(data_id_nr) + ";" + str(drehzahl) + ";" + str(leistungsaufnahme)  + ";" + str(vibration)  + ";" + str(lautstaerke) + "\n")
        zeile = zeile + 1
        x = x + 1
    # print("Wartung")
    return zeile

# Erstellung mehrerer Datensätze durch Schleife (Ausfall)
def ausfall(zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr):
    x = 1
    leistungsaufnahme = 18.5
    # Strombedarf steigt bis zum Ausfall
    while leistungsaufnahme < 25:
        drehzahl = 100 + random.randrange(-2, 2)
        leistungsaufnahme = round(np.random.normal(std_la*x, 0.2),3)
        vibration = round(np.random.normal(std_vb, 0.1),3)
        lautstaerke = round(np.random.normal(std_ls, 0.1),3)
        data_id_nr = 10000000 + zeile
        d.write("ABC" + str(data_id_nr) + ";" + str(drehzahl) + ";" + str(leistungsaufnahme)  + ";" + str(vibration)  + ";" + str(lautstaerke) + "\n")
        zeile = zeile + 1
        x = x + round(np.random.normal(0.01, 0.01),3)
    # zufällige Ausfallzeit
    x = 0
    y = random.randrange(1, 50)
    while x < y:
        drehzahl = 0
        leistungsaufnahme = round(np.random.normal(std_la*0.2, 0.1),3)
        vibration = round(np.random.normal(std_vb*2, 0.1),3)
        lautstaerke = round(np.random.normal(std_ls*0.3, 0.1),3)
        data_id_nr = 10000000 + zeile
        d.write("ABC" + str(data_id_nr) + ";" + str(drehzahl) + ";" + str(leistungsaufnahme)  + ";" + str(vibration)  + ";" + str(lautstaerke) + "\n")
        zeile = zeile + 1
        x = x + 1
    # print("Ausfall")
    return zeile

# Auswahl zwischen den Events
def choose(zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr):
    random_choice = random.randrange(1, 100)
    if random_choice < 80:
        zeile = str(normalbetrieb(zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr))   
    elif random_choice < 95:
        zeile = str(wartung(zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr))
    else:
        zeile = str(ausfall(zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr))
    #print(zeile)
    return zeile

# Aufruf Auswahl
while zeile < menge:
    zeile = int(choose(zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr))

# Timestamp am Ende der Datei erstellen
d.write(time.strftime("%d.%m.%Y %H:%M:%S"))

# Erfolgsbestätigung
dmount = zeile - 1
print("Datei mit " + str(dmount) + " Datensätzen wurde erstellt! Programm beendet")

# Schließen der Datei
d.close()
