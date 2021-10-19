'''
Acest script creaza randuri si table cu ajutorul inheritance-ului de clasa.
'''

import json


class JSONOutput:
    def __init__(self, *args, **kwargs):
        pass

    def to_json(self):
        return json.dumps(self)


class SimpleRow(dict, JSONOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _header(self):
        header_width = max(len(str(k)) for k in self)
        header_values = " | ".join(str(k).center(header_width) for k in self)
        return f"| {header_values} |"

    def _values(self):
        values_width = max(len(str(k)) for k in self)
        header_values = " | ".join(str(v).center(values_width) for v in self.values())
        return f"| {header_values} |"

    def show_table(self):
        return f"{self._header()} \n{self._values()}"


class SimpleTable(list, JSONOutput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _header(self, element):
        header_width = max(len(str(k)) for k in element)
        header_values = " | ".join(str(k).center(header_width) for k in element)
        return f"| {header_values} |"

    def _values(self, element):
        values_width = max(len(str(k)) for k in element)
        header_values = " | ".join(str(v).center(values_width) for v in element.values())
        return f"| {header_values} |"

    def print_table(self):
        for index, element in enumerate(self):
            if index == 0:
                print(self._header(element))
            print(self._values(element))


row1 = SimpleRow(no=1, name="Mark", surname="O'Connor", nationality="Irish")
row2 = SimpleRow(no=2, name="Mike", surname="O'Connor", nationality="Italian")
row3 = SimpleRow(no=3, name="John", surname="O'Connor", nationality="Romanian")

table = SimpleTable()
table1 = [row1, row2, row3]
print("-" * 57)
table.extend(table1)
table.print_table()
print("-" * 57)