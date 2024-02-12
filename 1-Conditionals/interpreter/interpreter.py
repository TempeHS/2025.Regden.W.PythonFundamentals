x = float(input("What's x? "))
y = float(input("What's y? "))
z = input("What you want them to do? ")

match z:
    case "+":
        print(x + y)
    case "-":
        print(x - y)
    case "/":
        print(x / y)
    case "*":
        print(x * y)
