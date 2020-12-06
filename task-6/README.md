# Readme

## Pliki - wykorzystane funkcje

**_\_\_file\_\__** - metoda specjalna, zwracająca ścieżkę do pliku.

**_open()_** - funkcja pozwalająca na otwarcie pliku w jednym z trybów (domyślnie do odczytu - 'r'). Tryb 'w' pozwala na zapis do pliku, z kolei dzięki trybowi 'a' możemy dodać coś do istniejącej zawartości. Poprzez 'rb', 'wb' przechodzimy w tryb bajtowy.

**_close()_** - zamykanie otwartego wcześniej pliku przy pomocy open(). Jest to bardzo ważne, by pamiętać o jak najszybszym zamykaniu pliku. Najlepeiej zaraz po zakończeniu pracy nad nim. Pomocne tutaj jest wyrażenie with, które zawsze automatycznie zamknie plik.

**_read()_** - odczytanie całej zawartości pliku lub poprzez wskazanie argumentu daną jego ilość znaków. 

**_readline()_** - odczytanie jednej linii z pliku lub poprzez wskazanie argumentu daną jej ilość znaków. 

**_readlines()_** - odczytanie wszystkich linii w tekście i zapisana jako lista.

**_write()_** - zapisanie do pliku wskazanego łańcucha znaków.

## dos2unix
Skrypt umożliwiający konwersję pliku z systemu Windows (znaki \r\n) na Unix (znaki \n).

## FileReade
Utworzyłem własną klasę odczytującą plik z 2 metodami:
**_\_\_enter\_\__** - funkcja wywołana przez 'with' w czasie otworzenia pliku
**_\_\_exit\_\__** - funkcja wywoływana przez 'with' w czasie zamknięcia pliku

## PngReader
Klasa umożliwiająca na odczyt pliku PNG bez nagłówków. Co pozwala na łatwy odczyt właściwych danych. 