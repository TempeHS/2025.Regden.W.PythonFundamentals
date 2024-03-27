import random


def main():
    while True:
        try:
            num = int(input("level: "))
            if num < int(1):
                print("invalid number")
                continue
            randnum = random.randint(1, num)
            while True:
                guess = numguess()
                if guess > num:
                    print("invalid number")
                elif guess < int(1):
                    print("invalid number")
                elif guess < randnum:
                    print("Too Small!")
                elif guess > randnum:
                    print("Too Large!")
                    continue
                else:
                    print("Just Right!")
                    break
            break
        except ValueError:
            print("invalid num")


def numguess():
    while True:
        try:
            guess = int(input("guess the number "))
            return guess
        except ValueError:
            print("invalid number")


main()
