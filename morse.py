class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
      
    def __str__(self):
        output = []
        for blip in self.pattern:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)

    # Write a class method named from_string that takes a string like "dash-dot"
    # and creates an instance with the correct pattern (['_', '.']).

    @classmethod
    def from_string(cls, dashdot_str):
        pattern = []
        for pat in dashdot_str.split('-'):
            if pat == "dash":
                pattern.append('_')
            elif pat == "dot":
                pattern.append('.')
        return cls(pattern)

class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)

    def __iter__(self):
        yield from self.pattern


letter = Letter()
wrong_pattern = "dash-dot"
print(letter.from_string(wrong_pattern))
