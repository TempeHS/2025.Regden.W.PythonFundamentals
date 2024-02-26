s = input("Say Something ")
c = s.split()

for letter in s:
    if letter == letter.upper():
        print("_", letter.lower(), sep="", end="")
    else:
        print(letter, end="")
