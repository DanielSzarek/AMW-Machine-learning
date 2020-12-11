# Readme

## JSON
*_json.dump()_* - serializacja obiektu wskazanego w pierwszym argumencie (obj) do JSON i zapis do pliku - drugi argument (fp)

*_json.dumps()_* - serializacja obiektu wskazanego w pierwszym argumencie (obj) do JSON. Możliwość określenia ilości spacji wciecia poprzez: _indent_.

*_json.load()_* - deserializacja JSONa z pliku na odpowiedni obiekt Python.

*_json.loads()_* - deserializacja JSONa ze stringa na odpowiedni obiekt Python. Mamy możliwosc utworzenia wlasnie deserializatora.

*_json.JSONEncoder_* - przy pomocy tej klasy możemy utworzyć własną klasę po niej dziedziczącą, która umożliwi implementacje serializacji dla specyficznego typu

## JSON - pomocnicze metody

*_requests.get()_* - wysyłka żadania HTTP GET

*_sorted()_* - funckja zwraca nową posortowaną listę, możemy określić szczegółowo sortowanie

*_join()_* - ma wiele zastosować. Zarówno łączy pojedyczne stringi, jak i te zawarte w listach. Poza tym ułatwia tworzenie ścieżek i URL.

*_filter()_* - filtruje przekazaną listę według zadanej funkcji

*_isinstance()_* - funkcja sprawdza, czy obiekt jest zadanego typu. Zwraca true/false.

## CSV

*_csv.reader()_* - odczytuje każdy obiekt, który iteruje linia po linii. Zwraca obiekt z możliwości iteracji po nim. Możemy wskazać co oddziela kolejne wartości np. przecinek w CSV.

*_csv.DictReader()_* - zwraca obiekt, który przekształcił linie pliku CSV w słownik (dict).

*_csv.writer()_* - funkcja zwraca obiekt, który pomoże w zapisie obiektu do pliku CSV. Możemy wskazać, co będzie oddzielało wartości w pliku.

*_csv.DictWriter()_* - funkcja zwraca obiekt, który pomoże w zapisie obiektu do pliku CSV ze słowników.

## CSV i Pandas

*_pandas.read_csv()_* - funkcja odczytuje plik CSV i przekstałca go od razu na obiekt DataFrame. Daje dużo możliwości, np. określenie, która kolumna jest indeksem.

*_DataFrame.to_csv()_* - funkcja umożliwia zapisu obiektu DataFrame do pliku CSV.





