fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
}
search = input("which fruit you want? ")
if search in fruits:
    print("calories:", fruits[search])
else:
    print("that is not a fruit")
