# machine data creation tool for machine learning project
# dorian zwanzig 2018-11-03
# version 0.2.1811121016

import numpy as np
import sys
import random
import time
from datetime import datetime, timedelta

# Zugriffsversuch auf Ausgabedatei
try:
    d = open("output.txt", "w")
except:
    print("Zugriff nicht erfolgt")
    sys.exit(0)

# Kopfzeile schreiben
d.write("ID;Uhrzeit;Drehzahl;Leistungsaufnahme;Vibration;Lautstaerke;Temperatur;FehlerID\n")

# Startwerte (STartData):
std_dz = 100             # Standarddrehzahl
std_la = 18.5            # Standardleistungsaufnahme
std_vb = 0               # Standardvibration
std_ls = 75              # Standardlautstärke
data_id_nr = 10000000    # Startwert für die ID Erstellung
std_te = 100             # Standardtemperatur
fehler_id = "leer"       # Fehlerwert bei Ausfall
time = datetime(2018, 1, 1, 0, 0, 0)   # Startzeit der Simulation

# Startzeile setzen
zeile = 1

# Nutzerabfrage: Menge Datensätze
menge = int(input("Bitte Anzahl der gewünschten Datensätze eingeben: ")) + zeile

# Werte in Ausgabedatei schreiben


def write_data():
    d.write("ABC" + str(data_id_nr) + ";" + str(time) + ";" + str(std_dz) + ";" + str(std_la) +
            ";" + str(std_vb) + ";" + str(std_ls) + ";" + str(std_te) + ";" + str(fehler_id) + "\n")

# Erstellung mehrerer Datensätze durch Schleife (Normalbetrieb)


def normalbetrieb():
    global zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr, std_te, time, fehler_id
    x = 0
    y = random.randrange(1, 200)
    while x < y:
        std_dz = 100
        std_la = round(np.random.normal(18.5, 0.1), 3)
        std_vb = round(np.random.normal(0, 0.1), 3)
        std_ls = round(np.random.normal(75, 0.1), 3)
        data_id_nr = data_id_nr + 1
        time = time + timedelta(seconds=30)
        std_te = 100
        fehler_id = "0000"
        write_data()
        zeile = zeile + 1
        x = x + 1

# Erstellung mehrerer Datensätze durch Schleife (Wartung)


def wartung():
    global zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr, std_te, time, fehler_id
    fehler_id = wartung_grund()
    x = 0
    y = random.randrange(10, 50)
    while x < y:
        std_dz = 0
        std_la = round(np.random.normal(2, 0.1), 3)
        std_vb = round(np.random.normal(0, 0.3), 3)
        std_ls = round(np.random.normal(25, 0.1), 3)
        time = time + timedelta(seconds=30)
        std_te = std_te - 1
        write_data()
        zeile = zeile + 1
        x = x + 1

# Wartungsgrund auswählen


def wartung_grund():
    random_choice = random.randrange(1, 100)
    if random_choice < 40:
        return "A001"   # Materialvorrat aufgebraucht (A001)
    elif random_choice < 70:
        return "A002"   # Werkzeugwechsel (A002)
    elif random_choice < 80:
        return "A003"   # Wartung (A003)
    elif random_choice < 95:
        return "A004"   # Reinigung (A004)
    else:
        return "A000"   # unbekannt (A000)

# Erstellung mehrerer Datensätze durch Schleife (Ausfall aufgrund zu hoher Motortemperatur)


def ausfall_2():
    global zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr, std_te, time, fehler_id
    fehler_id = "0000"
    x = 1
    # Motortemperatur steigt bis zum Ausfall
    while std_te < 200:
        std_dz = 100 + random.randrange(-2, 2)
        std_la = round(np.random.normal(18.5*x, 0.2), 3)
        std_vb = round(np.random.normal(0, 0.1), 3)
        std_ls = round(np.random.normal(75, 0.1), 3)
        data_id_nr = data_id_nr + 1
        time = time + timedelta(seconds=30)
        std_te = round(std_te + np.random.normal(1, 0.5), 1)
        write_data()
        zeile = zeile + 1
        x = x + round(np.random.normal(0.005, 0.002), 3)
    fehler_id = "F002"
    # Abkühlung bis Normaltemperatur bevor Maschine wieder angeschaltet wird
    while std_te > 100:
        std_dz = 0
        std_la = round(np.random.normal(1.5, 0.1), 3)
        std_vb = round(np.random.normal(0, 0.05), 3)
        std_ls = round(np.random.normal(25, 0.1), 3)
        data_id_nr = data_id_nr + 1
        std_te = round(std_te - 1, 1)
        time = time + timedelta(seconds=30)
        write_data()
        zeile = zeile + 1
        x = x + 1
    return zeile

# Erstellung mehrerer Datensätze durch Schleife (Ausfall aufgrund zu hoher Leistungsaufnahme)


def ausfall_1():
    global zeile, menge, std_dz, std_la, std_vb, std_ls, data_id_nr, std_te, time, fehler_id
    fehler_id = "0000"
    x = 1
    # Strombedarf steigt bis zum Ausfall
    while std_la < 25:
        std_dz = 100 + random.randrange(-2, 2)
        std_la = round(np.random.normal(18.5*x, 0.2), 3)
        std_vb = round(np.random.normal(0, 0.1), 3)
        std_ls = round(np.random.normal(75, 0.1), 3)
        data_id_nr = data_id_nr + 1
        time = time + timedelta(seconds=30)
        std_te = round(std_te + np.random.normal(0.5, 0.2), 1)
        write_data()
        zeile = zeile + 1
        x = x + round(np.random.normal(0.01, 0.005), 3)
    fehler_id = "F001"
    # zufällige Ausfallzeit
    x = 0
    y = random.randrange(10, 50)
    while x < y:
        std_dz = 0
        std_la = round(np.random.normal(1.5, 0.1), 3)
        std_vb = round(np.random.normal(0, 0.1), 3)
        std_ls = round(np.random.normal(25, 0.1), 3)
        data_id_nr = data_id_nr + 1
        std_te = round(std_te - 1, 1)
        time = time + timedelta(seconds=30)
        write_data()
        zeile = zeile + 1
        x = x + 1
    return zeile

# Auswahl zwischen den Events


def choose():
    random_choice = random.randrange(1, 100)
    if random_choice < 60:
        normalbetrieb()
    elif random_choice < 80:
        wartung()
    elif random_choice < 90:
        ausfall_1()
    else:
        ausfall_2()


# Aufruf Auswahl
while zeile < menge:
    choose()

# Erfolgsbestätigung
counter = zeile - 1
print("Datei mit " + str(counter) +
      " Datensätzen wurde erstellt! Programm beendet")

# Schließen der Datei
d.close()
