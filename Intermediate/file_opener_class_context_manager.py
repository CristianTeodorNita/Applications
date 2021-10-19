'''
Acest script prezinta un context manager ca si clasa utilizat pentru a deschide si inchide un fisier automat.
'''


class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.openedObject = None

    def __enter__(self):
        print(f"Hey, am deschis fisierul {self.filename}")
        self.openedObject = open(self.filename, self.mode)
        return self.openedObject

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Hey, am inchis in siguranta fisierul {self.filename}")
        self.openedObject.close()


def read_from_file(filename):
    with FileOpener(filename, "r") as f:
        print(f.read())
