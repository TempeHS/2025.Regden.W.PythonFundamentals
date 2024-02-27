def main():
    coke = 50
    while coke > 0:
        coin = int(input("Insert a coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            coke -= coin
            if coke > 0:
                print("Amount due:", coke)
            else:
                print("Change owed:", -coke)
        else:
            print("Amount due:")


main()
