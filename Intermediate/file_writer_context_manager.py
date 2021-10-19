'''
Acest modul implementeaza hand-made context manager ca si clasa pentru a putea scrie din fisiere si a cronometra timpul.
'''

import datetime

utc_time = datetime.datetime.now().strftime("%c\nMinute: %M, Second: %S")


class FileWriter:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.open_time = datetime.datetime.now().strftime("%c\nMinute: %M, Second: %S")

    def __sub__(self, other):
        return self.close_time - other.close_time

    def __enter__(self):
        print(f"Hey, timpul deschiderii fisierului este {self.open_time}")
        self.openedObject = open(self.filename, self.mode)
        return self.openedObject

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_time = datetime.datetime.now().strftime("%c\nMinute: %M, Second: %S")
        time_passed = self.close_time - self.open_time
        print(f"Hey, am inchis in siguranta fisierul {self.filename} iar timpul executiei a fost {time_passed}")
        self.openedObject.close()
