class CustomList:
    def __init__(self, initial=None):
        self._data = initial if initial is not None else []

    def append(self, value):
        self._data.append(value)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f"CustomList({self._data})"

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __eq__(self, other):
        if not isinstance(other, CustomList):
            return False
        return self._data == other._data

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

cl = CustomList([1, 2, 3])

cl.append(4)

print(cl)
print(len(cl))
print(cl[1])

for item in cl:
    print(item)

print(2 in cl)