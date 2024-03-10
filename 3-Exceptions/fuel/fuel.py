def fractionator():
    while True:
        try:
            fraction = input("enter fuel is (x/y): ")
            top, bot = map(int, fraction.split("/"))
            if top < 0 or bot <= 0:
                raise ValueError
            return top, bot
        except (ValueError, ZeroDivisionError):
            print("Doesn't work ")


def main():
    while True:
        try:
            top, bot = fractionator()
            fuel = float(top / bot) * int(100)
            rfuel = round(fuel)
            if top > bot:
                raise ValueError
            elif rfuel < int(1):
                print("E")
            elif rfuel > int(99):
                print("F")
            else:
                print(rfuel, "%", sep="")
            break
        except ValueError:
            print("dont work")


main()
