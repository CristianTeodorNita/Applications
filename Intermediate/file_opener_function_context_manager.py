'''
Acest script prezinta un context manager ca si functie utilizat pentru a deschide si inchide un fisier automat.
'''
from contextlib import contextmanager


@contextmanager
def FileOpener(filename, mode):
    print(f"Hey, am deschis fisierul {filename}")
    f = open(filename, mode)
    yield f
    print(f"Hey, am inchis in siguranta fisierul {filename}")
    f.close()


def file_reader(filename):
    with FileOpener(filename, "r") as f:
        print(f.read())
