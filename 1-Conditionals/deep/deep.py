meaning = input("What is the answer to the Great Question of Life? ")

match meaning:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
