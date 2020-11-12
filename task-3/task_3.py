import numpy as np
import pandas as pd
from scipy import linalg, sparse
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure
from bokeh.io import output_file, show


def python_basics():
    print("PYTHON BASICS")
    print("================================================")

    my_number_list = [20, 4, 7, 92, 1337, 15, 33, 70, -100]
    my_string_list = ['This', 'is', 'a', 'list', 'of', 'strings']

    print("1. Pobranie ostatnich 3 elementów listy:")
    print(my_string_list[-3:])

    print("2. Dodanie elementu do listy:")
    my_string_list.append('!')
    print(my_string_list)

    print("3. Sortowanie listy:")
    print(my_number_list)
    my_number_list.sort()
    print(my_number_list)

    print("4. Odwrócenie listy:")
    my_number_list.reverse()
    print(my_number_list)

    print("5. Usunięcie wszystkich elementów oprócz pierwszego i ostatniego")
    del(my_number_list[1:-1])
    print(my_number_list)


def numpy_basics():
    print("\nNUMPY BASICS")
    print("================================================")

    numpy_array = np.random.random((4, 4))

    print("1. Kopiowanie listy:")
    numpy_array_copy = numpy_array.copy()
    print(numpy_array_copy)

    print("2. Sprawdzenie typów elementów macierzy")
    print(numpy_array_copy.dtype)

    print("3. Dodanie do siebie macierzy")
    new_numpy_array = np.add(numpy_array, numpy_array_copy)
    print(new_numpy_array)

    print("4. Sortowanie elementów macierzy")
    new_numpy_array.sort()
    print(new_numpy_array)

    print("5. Dodanie wszystkich elementów macierzy:")
    print(new_numpy_array.sum())


def scipy_basics():
    print("\nSCIPY BASICS")
    print("================================================")
    matrix = np.mat(np.random.random((5, 5)))

    print("1. Obliczenie normy macierzowej:")
    print(linalg.norm(matrix))

    print("2. Obliczenie pseudo-inwersji macierzy:")
    print(linalg.pinv(matrix))

    print("3. Wyznacznik macierzy:")
    print(linalg.det(matrix))

    print("4. Skompresowana macierz rozsianych wierszy")
    print(sparse.csr_matrix(matrix))

    print("5. Macierz wykładnicza")
    print(linalg.expm(matrix))


def pandas_basics():
    print("\nPANDAS BASICS")
    print("================================================")
    data = {
        'group': ['175IC_A1', '172IC_A1', '175IC_B1', '175IC_B2', '175IC_A2', '172IC_A2'],
        'civil': [True, False, True, True, True, False],
        'students_amount': [25, 20, 20, 20, 15, 30]
    }
    df = pd.DataFrame(data)

    print("1. Podsumowanie DataFrame dla wartości liczbowych:")
    print(df.describe())

    print("2. Wypisanie wszystkich grup:")
    print(df.iloc[0:, 0])

    print("3. Wypisanie średniej liczby osób w grupe:")
    print(df.loc[:, 'students_amount'].mean())

    print("4. Wypisanie ilości grup cywilnych:")
    print(df.loc[:, 'civil'].sum())

    print("5. Posortowanie grup po ilości studentów:")
    print(df.sort_values(by='students_amount'))


def scikit_learn():
    print("\nSCIKIT BASICS")
    print("================================================")
    data = {
        'group': ['175IC_A1', '172IC_A1', '175IC_B1', '175IC_B2', '175IC_A2', '172IC_A2'],
        'civil': [True, False, True, True, True, False],
        'students_amount': [25, 20, 25, 20, 15, 30]
    }
    df = pd.DataFrame(data)

    print("1. Przygotowanie do pracy na danych przy pomocy fit_transform")
    le = LabelEncoder()
    df['civil'] = le.fit_transform(df['civil'])
    print(df)

    print("2. Podział na dane uczące i dane testowe")
    df_input = df[['students_amount']]
    df_output = df['civil']
    x_train, x_test, y_train, y_test = train_test_split(df_input, df_output)
    print(x_train)
    print(y_train)

    print("3. Dopasowanie modelu:")
    clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    clf.fit(x_train, y_train)
    Pipeline(steps=[('standardscaler', StandardScaler()),
                    ('svc', SVC(gamma='auto'))])
    print("4. Przewidywanie dla konkretnej wartości:")
    print(clf.predict([[20]]))
    print(clf.predict([[30]]))

    print("5. Przewidywanie poprzez algorytm kmeans - nauczanie bez nadzoru")
    k_means = KMeans(n_clusters=3, random_state=0)
    k_means.fit(x_train, y_train)
    y_pred = k_means.predict(x_test)
    print(x_test)
    print(y_pred)


def matplotlib_basics():
    print("\nMATPLOTLIB BASICS")
    print("================================================")

    x = np.linspace(-5, 5, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    print("1. Utworzenie obiektu z wykresem")
    plot_figure = plt.figure()

    print("2. Dodanie możliwości utworzneia większej ilości wykresów na 1 polu")
    axes = plot_figure.add_subplot(111)

    print("3. Dodanie danych do wykresu i określenie ich typu")
    axes.plot(x, y_sin)
    axes.plot(x, y_cos)
    axes.scatter(x, y_sin, marker='.')
    axes.scatter(x, y_cos, marker='*')

    print("4. Dodanie tytułu")
    plt.title('Sinus and Cosinus')

    print("5. Zapis wykresu do pliku")
    plt.savefig('sin_cos.png')

    print("6. Wyświetlenie wykresu")
    plt.show()


def seaborn_basics():
    print("\nSEABORN BASICS")
    print("================================================")

    print("1. Ładujemy dane z repozytorium: planets")
    planets = sns.load_dataset("planets")

    print("2. Ustawiamy styl wykresu")
    sns.set_style("whitegrid")

    print("3. Wykres punktowy")
    sns.pointplot(
        x="year",
        y="mass",
        hue="method",
        data=planets
    )
    plt.show()

    print("4. Wykres słupkowy")
    sns.barplot(
        x="year",
        y="method",
        data=planets
    )
    plt.show()

    print("5. Wykres skrzypkowy")
    sns.barplot(
        x="number",
        y="distance",
        hue="method",
        data=planets
    )
    plt.show()


def bokeh_basics():
    print("\nBOKEH BASICS")
    print("================================================")
    x = [1, 2, 3, 4, 5]
    y = [5000, 4700, 4500, 3000, 2850]

    print("1. Utworzenie wykresu")
    plot = figure(
        title="Money balance",
        x_axis_label='day',
        y_axis_label='money'
    )

    print("2. Utworzenie legendy oraz orientacja wykresu")
    plot.line(x, y, legend_label="Money", line_width=4)
    plot.legend.orientation = "vertical"
    print("3. Ustawienie koloru")
    plot.legend.border_line_color = "blue"

    print("4. Nazwa dla utworzonego pliku html")
    output_file("money_balance.html")

    print("5. Otworzenie storny html z wykresem")
    show(plot)


if __name__ == "__main__":
    python_basics()
    numpy_basics()
    scipy_basics()
    pandas_basics()
    scikit_learn()
    matplotlib_basics()
    seaborn_basics()
    bokeh_basics()
