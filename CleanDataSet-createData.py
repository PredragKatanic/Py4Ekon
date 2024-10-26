# Neophodam je modul pandas
# pip install pandas

import pandas as pd
import random

# Definisanje ukupnog broja zapisa
total_records = 10000

# Definisanje listi mogućih vrednosti za svaku kolonu na početku
genders = ["Muško", "Žensko"]
categories = ["Odjeća", "Obuća", "Dodaci", "Spoljašnja odjeća"]
delivery_types = ["Besplatna dostava", "Ekspres", "Dvodnevna dostava", "Sledeći dan"]
professions = ["Zdravstvo", "Inženjer", "Pravnik", "Umjetnik", "Izvršni direktor", 
               "Marketing", "Doktor", "Upravitelj", "Ekonomista", "Nastavnik", "Dizajner", "Student", "Tehničar", ""]
seasons = ["Proljeće", "Ljeto", "Jesen", "Zima", ""]
municipalities = ["Sarajevo", "Banja Luka", "Tuzla", "Zenica", "Mostar", "Bihać", "Prijedor", 
                  "Sanski Most", "Gradiška", "Laktaši", "Široki Brijeg", "Bijeljina", "Živinice"]
items = ["Majica", "Haljina", "Cipele", "Farmerke", "Šorc", "Kaput", "Naočale", "Torba", "Šal", "Patike", "Kaiš"]
subscription_choices = ["Da", "Ne"]

# Generisanje podataka
data = {
    "KupacID": range(1, total_records + 1),
    "Pol": [random.choice(genders) for _ in range(total_records)],
    "Godine": [random.randint(18, 65) for _ in range(total_records)],
    "Kupljeni Artikli": [random.choice(items) for _ in range(total_records)],
    "Kategorija": [random.choice(categories) for _ in range(total_records)],
    "Iznos Kupovine": [random.randint(10, 100) for _ in range(total_records)],
    "Tip Dostave": [random.choice(delivery_types) for _ in range(total_records)],
    "Zanimanje": [random.choice(professions) for _ in range(total_records)],
    "Pretplata": [random.choice(subscription_choices) for _ in range(total_records)],
    "Sezona": [random.choice(seasons) for _ in range(total_records)],
    "Opština": [random.choice(municipalities) for _ in range(total_records)],
}

# Kreiranje DataFrame-a
df = pd.DataFrame(data)

# Sačuvaj u Excel
output_excel_path = "DataSet/DataSet4Clear.xlsx"
df.to_excel(output_excel_path, index=False)

# Sačuvaj u CSV
output_csv_path = "DataSet/DataSet4Clear.csv"
df.to_csv(output_csv_path, index=False)
