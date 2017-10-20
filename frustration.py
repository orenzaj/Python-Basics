# This class will give the wrong length from a given list.
# This exercise teaches method overloading

class Liar(list):
    def __len__(self):
        return super().__len__() + 3
        

