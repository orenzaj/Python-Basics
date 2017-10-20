def disemvowel(word):
    vowels = ["a", "e", "i", "o", "u"]
    return ''.join([i for i in word if i.lower() not in vowels])
    
print(disemvowel("TreehOUse"))
