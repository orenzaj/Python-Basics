import copy

class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):              # _ is a throwaway variable
            self.append(copy.copy(value))   


fl = FilledList(9,2)
fl2 = FilledList(5, [1, 4, 3])
fl2[0][1] = 10
print(fl)
print(fl2)
print(fl2[0][1])

