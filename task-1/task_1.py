import numpy as np

counter = 1


def mark_new_task():
    global counter
    print(f"\nTASK {counter}. ========================================================")
    counter += 1


mark_new_task()
print("Tablica zawierającą 10 zer")
zeroes = np.zeros(10)
print(zeroes)

mark_new_task()
print("Tablica zawierającą 10 piątek")
fifths = np.full(10, 5)
print(fifths)


mark_new_task()
print("Tablica zawierającą liczby od 10 do 50")
from_10_to_50 = np.arange(10, 50, 1)
print(from_10_to_50)

mark_new_task()
print("Macierz o wymiarach 3x3 zawierającą liczby od 0 do 8")
matrix = np.arange(9).reshape(3, 3)
print(matrix)

mark_new_task()
print("Macierz jednostkową o wymiarach 3x3")
identity_matrix = np.eye(3)
print(identity_matrix)

mark_new_task()
print("Macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej")
normal_distribution_matrix = np.random.normal(size=(5, 5))
print(normal_distribution_matrix)

mark_new_task()
print("Macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01")
matrix2 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(matrix2)

mark_new_task()
print("Tablica zawierającą 20 liniowo rozłożonych liczb między 0 a 1")
linspace = np.linspace(0, 1, 20)
print(linspace)

mark_new_task()
print("Tablicę zawierającą losowe liczby z przedziału (1, 25), zamieniona na macierz")
rand = np.random.randint(low=1, high=25, size=25).reshape(5, 5)
print(rand)
print("Suma wszystkich liczb w ww. macierzy")
print(rand.sum())
print("Średnia wszystkich liczb w ww. macierzy")
print(np.average(rand))
print("Standardowa dewiację dla liczb w ww. macierzy")
print(np.std(rand))
print("Suma każdej kolumny ww. macierzy")
print(rand.sum(axis=0))

mark_new_task()
print("Macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100)")
rand2 = np.random.randint(low=1, high=100, size=(5, 5))
print(rand2)
print("Mediana tych liczb")
print(np.median(rand2))
print("Najmniejsza liczbę tej macierzy")
print(rand2.min())
print("Największa liczbę tej macierzy")
print(rand2.max())

mark_new_task()
print("Macierz zawierającą losowe liczby z przedziału (0, 100) i transpozycja")
rand2 = np.random.randint(low=1, high=100, size=(5, 7))
print(rand2.T)

mark_new_task()
print("Suma dwóch macierzy")
matrix_a = np.random.randint(low=1, high=100, size=(4, 7))
matrix_b = np.random.randint(low=1, high=100, size=(4, 7))
print(matrix_a)
print(matrix_b)
print("Suma:")
print(np.add(matrix_a, matrix_b))

mark_new_task()
print("Mnożenie macierzy na 2 sposoby")
matrix_a = np.random.randint(low=1, high=100, size=(4, 5))
matrix_b = np.random.randint(low=1, high=100, size=(5, 4))
print(matrix_a)
print(matrix_b)
print("Mnożenie:")
print(np.matmul(matrix_a, matrix_b))
print(np.dot(matrix_a, matrix_b))


