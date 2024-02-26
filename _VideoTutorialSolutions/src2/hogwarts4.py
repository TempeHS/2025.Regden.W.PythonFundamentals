# Demonstrates iterating over and index into a dict

fruits = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for fruit in fruits:
    print(fruit, fruits[fruit], sep=", ")
