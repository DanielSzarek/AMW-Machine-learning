# Readme

## CV2
*_cv2.imread()_* - wczytanie obrazu jako "NumPy array", czyli wczytujemy obrazu i wrzucamy go do tablicy.

*_cv2.shape_* - własność pozwalająca na odczyt długości, szerokości i głebokość zdjęcia (liczba kanałów - RGB)

*_cv2.imshow()_* - wyświetlenie zdjęcia

*_cv2.waitKey()_* - oczekiwanie na klawisz 0, by zamknąć wyświetlany obraz

*_cv2.resize()_* - możliwość zmiany wielkości obrazu

*_getRotationMatrix2D()_* - obliczenie macierzy rotacji, wskazujemy kąt pod jakim ma odbyć się rotacja

*_cv2.warpAffine()_* - na podstawie macierzy rotacji oraz wysokości i szerokości funkcja obraca obraz

*_cv2.GaussianBlur()_* - zredukowanie jakości zdjęcia, pozwala to na skupić się wyłącznie na ważnych elementach w czasie późniejszego przetwarzania obrazu 

*_cv2.copy()_* - funckja zwraca kopię macierzy ze zdjęciem

*_cv2.rectangle()_* - rysowanie prostokąta, wskazujemy lewy górny i prawy dolny wierzchołek oraz kolor i grubość

*_cv2.circle()_* - rysowanie koła, wskazujemy środek i promień oraz kolor i grubość

*_cv2.line()_* - rysowanie linii, wskazujemy 2 punkty, kolor i grubość

*_cv2.putText()_* - dodanie tekstu na zdjęciu, wskazujemy teskt, miejsce, rodzaj oraz wielkość czcionki, kolor i grubość

*_cv2.cvtColor()_* - przekształcenie obrazu do odcieni szarości lub koloru 

*_cv2.Canny_* - Canny to klasa pomagająca w detekcji krawędzi

*_cv2.threshold()_* - funkcja pomaga w usuwaniu białych lub czarnych regionów z obrazu

*_cv2.drawContours()_* - funkcja rysuje kontur określonego obiektu

*_cv2.erode()_* - używamy erode, by zmniejszyć wielkość obiektów pierwszoplanowych

*_cv2.dilate()_* - odwrotnie jak erode, dilate zwiększa wielkość obiektów pierwszoplanowych

*_cv2.bitwise_and()_* - tło, a w zasadzie jasne pixele stają się czarne

## Imutils
*_imutils.resize()_* - możliwość zmiany wielkości obrazu, w tym przypadku nie musimy sami obliczać skali

*_imutils.rotate_* - podobnie jak przy resize() funkcja zapewnia mniej pracy przy chęci obrócenia zdjęcia - wystarczy podać kąt rotacji

*_imutils.rotate_bound_* - rotacja bez przycięcia zdjęcia

*_imutils.grab_contours_* - funkcja znajduje kontury w obrazie

## Argparse
*_ap.add_argument_* - dodanie argumentów startowych programu podczas uruchomienia skryptu