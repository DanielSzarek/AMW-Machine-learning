import numpy as np

counter = 1


def mark_new_task():
    global counter
    print(f"TASK {counter}. ========================================================")
    counter += 1


mark_new_task()
zeroes = np.zeros(10)
print(zeroes)

mark_new_task()
fifths = np.full(10, 5)
print(fifths)


mark_new_task()
from_10_to_50 = np.arange(10, 50, 1)
print(from_10_to_50)

mark_new_task()
matrix = np.arange(9).reshape(3, 3)
print(matrix)

mark_new_task()
identity_matrix = np.eye(3)
print(identity_matrix)

mark_new_task()
normal_distribution_matrix = np.random.normal(size=(5, 5))
print(normal_distribution_matrix)

mark_new_task()
matrix2 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(matrix2)

mark_new_task()
linspace = np.linspace(0, 1, 20)
print(linspace)

mark_new_task()
rand = np.random.randint(low=1, high=25, size=25).reshape(5, 5)
print(rand)
print(rand.sum())
print(np.average(rand))
print(np.std(rand))
print(rand.sum(axis=0))

mark_new_task()
rand2 = np.random.randint(low=1, high=100, size=(5, 5))
print(rand2)
print(np.median(rand2))
print(rand2.min())
print(rand2.max())

mark_new_task()
rand2 = np.random.randint(low=1, high=100, size=(5, 7))
print(rand2.T)

mark_new_task()
matrix_a = np.random.randint(low=1, high=100, size=(4, 7))
matrix_b = np.random.randint(low=1, high=100, size=(4, 7))
print(np.add(matrix_a, matrix_b))

mark_new_task()
matrix_a = np.random.randint(low=1, high=100, size=(4, 5))
matrix_b = np.random.randint(low=1, high=100, size=(5, 4))
print(np.matmul(matrix_a, matrix_b))
print(np.dot(matrix_a, matrix_b))


