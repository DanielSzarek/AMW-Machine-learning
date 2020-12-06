class FileReader:
    def __init__(self, file_path):
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path)
        print("Plik otwarty")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file_object.close()
        print("Plik zamknięty!")

