# An attribute starting with __

class Protected:
    __name = "Security"

    def __method(self):
        return self.__name

prot = Protected()      # prot is an instance of Protected
# prot.__name
# prot.__method()       # this won't show the name Attribute Error
# print(dir(prot))      # to look into it, check directory for method
print(prot._Protected__method())
print(prot._Protected__name)
