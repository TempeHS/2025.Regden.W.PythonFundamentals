def removevowel(words):
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    newword = words
    for letter in words:
        if letter in vowels:
            newword = newword.replace(letter, "")
    return newword


words = input("Say Something ")
newword = removevowel(words)
print(newword)
