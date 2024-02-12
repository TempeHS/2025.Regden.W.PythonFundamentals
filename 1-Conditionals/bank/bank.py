# if hello print $0
# elif h or no h boolean
# True print $20
# false Print $100


# .strip whitesapce
# .startswith for hello
# also .find for hello
# firstcharacter = str[:1]

greeting = input("How would you like to be greeted? ")
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("Hello"):
    print("$20")
elif greeting.startswith("h"):
    print("$20")
elif greeting.startswith("H"):
    print("$20")
else:
    print("$100")
