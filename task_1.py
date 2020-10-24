import numpy as np


def insert_brake():
    print("========================================================")


zeroes = np.zeros(10)
print(f"1. {zeroes}")
insert_brake()

fifths = np.full(10, 5)
print(f"2. {fifths}")
insert_brake()

from_10_to_50 = np.arange(10, 50, 1)
print(f"3. {from_10_to_50}")
insert_brake()

matrix = np.arange(9).reshape(3, 3)
print(f"4. {matrix}")
insert_brake()

identity_matrix = np.eye(3)
print(f"5. {identity_matrix}")
insert_brake()

normal_distribution_matrix = np.random.normal(size=(5, 5))
print(f"6. {normal_distribution_matrix}")
insert_brake()

matrix2 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(f"7. {matrix2}")
insert_brake()

linspace = np.linspace(0, 1, 20)
print(f"8. {linspace}")
insert_brake()

rand = np.random.randint(low=1, high=25, size=25).reshape(5, 5)
print(f"9. {rand}")
print(rand.sum())
print(np.average(rand))
print(np.std(rand))
print(rand.sum(axis=0))
insert_brake()

rand2 = np.random.randint(low=1, high=100, size=(5, 5))
print(f"10. {rand2}")
print(np.median(rand2))
print(rand2.min())
print(rand2.max())
insert_brake()

rand2 = np.random.randint(low=1, high=100, size=(5, 7))
print(f"11. {rand2.T}")
insert_brake()

matrix_a = np.random.randint(low=1, high=100, size=(4, 7))
matrix_b = np.random.randint(low=1, high=100, size=(4, 7))
print(f"12. {np.add(matrix_a, matrix_b)}")
insert_brake()

matrix_a = np.random.randint(low=1, high=100, size=(4, 5))
matrix_b = np.random.randint(low=1, high=100, size=(5, 4))
# print(np.multiply(matrix_a, matrix_b))
print(f"13. {np.matmul(matrix_a, matrix_b)}")


