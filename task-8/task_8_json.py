import json
import os
from task_8_sport import Sport

counter = 1


def new_task():
    global counter
    print(f"\n{counter}. ========================================================")
    counter += 1


data = {
    "sport": {
        "name": "football",
        "players": 11
    }
}

new_task()
with open('data_file.json', 'w') as file:
    json.dump(data, file)

print(json.dumps(data, indent=4))

new_task()
with open('data_file.json', 'r') as file:
    data_from_file = json.load(file)
    print(data_from_file)

new_task()
os.system("python task_8_json_request.py")

new_task()
sport = Sport('football', True, 11)

try:
    json.dumps(sport)
except Exception as e:
    print(str(e))

new_task()
complex_object = 3 + 7j


def encode(object: complex):
    if isinstance(object, complex):
        return (object.real, object.imag)
    else:
        type_name = object.__class__.__name__
        print(f"Object of type {type_name} is not serializable")


complex_json = json.dumps(complex_object, default=encode)
print(complex_json)

new_task()
class ComplexEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, complex):
            return (object.real, object.imag)
        else:
            return super().default(object)


complex_json = json.dumps(complex_object, cls=ComplexEncoder)
print(complex_json)


def decode_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct

with open('complex.json', 'r') as reader:
    data = reader.read()
    complex_object = json.loads(data, object_hook=decode_complex)
    print(complex_object)

with open('complex_numbers.json', 'r') as reader:
    data = reader.read()
    numbers = json.loads(data, object_hook=decode_complex)
    print(numbers)