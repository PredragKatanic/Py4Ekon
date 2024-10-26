## Generisanje i Izvoz Nasumičnih Podataka

Ovaj Python kod koristi biblioteku `pandas` za generisanje nasumičnog skupa podataka sa 10.000 zapisa, prilagođenih strukturiranju informacija o kupcima. Korišćenjem različitih listi za atribute kupaca, kod omogućava generisanje podataka i njihovo čuvanje u Excel i CSV formatu. Kroz jednostavnu promenu ukupnog broja zapisa, lako je generisati veće ili manje količine podataka.

Potrebno je prethodno instalirati `pandas` modul
``` bash
pip install pandas
```
### Struktura Koda

1. **Definisanje Broja Zapisa**
   - Na početku, kod koristi promenljivu `total_records` koja označava ukupan broj zapisa koji će biti generisani. Ova vrednost se lako može prilagoditi mijenjanje definisanog proja redova.

2. **Definisanje Listi**
   - Za svaki red u zapisu definišemo naziv kolone (atribut) i vrijednosti koje može da preuzme, Te vrijednosti su definisane kroz liste sa mogućim vrednostima atributa:
     - `genders`: Pol kupca (Muško/Žensko)
     - `categories`: Kategorija kupljenog artikla (npr. Odjeća, Obuća)
     - `delivery_types`: Tip dostave (npr. Besplatna dostava, Ekspres)
     - `professions`: Zanimanje kupca (npr. Zdravstvo, Inženjer)
     - `seasons`: Sezona kada je obavljena kupovina (Proljeće, Ljeto)
     - `municipalities`: Opštine (gradovi) iz kojih kupci dolaze
     - `items`: Lista proizvoda koji su kupljeni (Majica, Haljina itd.)
     - `subscription_choices`: Status pretplate (Da/Ne)

3. **Generisanje Podataka**
   - Koristeći `random.choice`, kod nasumično bira vrednosti iz ovih listi za svaki atribut.
   - Na primer, za pol kupca, kod bira između "Muško" i "Žensko", a za godine kupaca, nasumična vrednost između 18 i 65.

4. **Kreiranje DataFrame-a**
   - Nakon što se generišu sve vrednosti, one se kombinuju u `pandas` DataFrame za dalju obradu i izvoz.

5. **Izvoz u Excel i CSV**
   - Kod eksportuje DataFrame u dva formata:
     - **Excel**: `DataSet4Clear.xlsx`
     - **CSV**: `DataSet4Clear.csv`

Ovaj način generisanja podataka olakšava testiranje aplikacija i razvoj sistema koji zahtevaju nasumične skupove podataka za analize i simulacije.
