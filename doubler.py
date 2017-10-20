# This class will double whatever it's given as parameter.

class Double(int):
    def __new__(*args, **kwargs):
        self = int.__new__(*args, **kwargs)
        return self * 2

print(Double(3))
