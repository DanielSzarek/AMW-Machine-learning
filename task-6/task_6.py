from my_file_reader import FileReader
from my_png_reader import PngReader

counter = 1


def mark_new_task():
    global counter
    print(f"\n{counter}. ========================================================")
    counter += 1


mark_new_task()
reader = open("21169_szarek.txt", 'r')
reader_bytes = open("21169_szarek.txt", 'rb')
try:
    print(type(reader))
    print(type(reader_bytes))
finally:
    reader.close()
    reader_bytes.close()

mark_new_task()
with open('21169_szarek.txt', 'r') as reader:
    print(reader.read())

mark_new_task()
with open('21169_szarek.txt', 'rb') as reader:
    print(reader.readlines(5))

mark_new_task()
f = open('21169_szarek.txt', 'rb')
print(list(f))

mark_new_task()
with open('21169_szarek.txt', 'r') as reader:
    for line in reader:
        print(line, end='')

mark_new_task()
with open('21169_szarek.txt', 'r') as reader:
    text = reader.readlines()

with open('21169_szarek_reversed.txt', 'w') as writer:
    for line in reversed(text):
        writer.write(line)

mark_new_task()
with open('Nature_celebrating_India.png', 'rb') as reader:
    print(reader.read(1))
    print(reader.read(3))
    print(reader.read(2))
    print(reader.read(1))
    print(reader.read(1))

mark_new_task()
print(__file__)

mark_new_task()
with open('21169_szarek.txt', 'a') as writer:
    writer.write("\nNew line")

mark_new_task()
with FileReader('21169_szarek_my_reader.txt') as reader:
    pass

mark_new_task()
with PngReader('Nature_celebrating_India.png') as reader:
    for l, t, d, c in reader:
        print(f"{l:05}, {t}, {c}")