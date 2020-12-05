import pandas as pd
import matplotlib.pyplot as plt


counter = 1


def mark_new_task():
    global counter
    print(f"\nZadanie {counter}. ========================================================")
    counter += 1


cars = pd.read_csv('samochody1tys.csv')

# 1. Wyświetlenie podstawowego opisu wczytanych danych
mark_new_task()
print(cars.describe())

# 2. Wypisanie rozmiaru DataFrame
mark_new_task()
print(cars.shape)

# 3. Wyświetla auta droższe od 500 000 zł
mark_new_task()
cars_brand_price = cars[cars["cena"] > 500000]
print(cars_brand_price)

# 4. Sortuje auto od ceny najniższej
mark_new_task()
print(cars.sort_values('cena', ascending=True))

# 5. Zmiana nazw wyświetlanych nazw kolumn
mark_new_task()
print(cars.rename(columns={
    'id': 'Indeks',
    'marka': 'Marka',
    'model': 'Model',
    'rok_produkcji': 'Rok produkcji',
    'rodzaj_silnika': 'Rodzaj silnika',
    'pojemnosc_silnika': 'Pojemność silnika',
    'przebieg': 'Przebieg (km)',
    'cena': 'Cena (zł)',
    'wojewodztwo': 'Województwo'
}))

# 6. Wypisanie tylko rzędów 100-105 wraz z kolumnami 3-6
mark_new_task()
print(cars.iloc[100:105, 3:6])

# 7. Wykres oparty o nasz zbiór danych
mark_new_task()
cars.plot.scatter(x='cena', y='wojewodztwo')
plt.show()

# 8. Wypisanie tylko marek Audi z ceną poniżej 10 000 zł
mark_new_task()
cars_query = cars.query(
    'marka == "Audi" and rok_produkcji < 2005 and cena <= 10000'
)
print(cars_query)

# 9. Pogrupowane wartości średnie według roku produkcji z wykluczeniem klumny indeks
mark_new_task()
print(cars.drop(columns=["id"]).groupby(["rok_produkcji"]).mean())

# 10. Serializacja pierwszego rekordu do jsona
mark_new_task()
cars_json = cars.head(1).to_json(indent=4)
print(cars_json)
