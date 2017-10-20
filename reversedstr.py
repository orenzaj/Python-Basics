class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]                   # Reverse
        return self

print(ReversedStr("hello"))
