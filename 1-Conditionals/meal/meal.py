def convert(time: str):
    hours, minutes = time.split(":")
    x = float(minutes) / 60
    z = float(hours) + x
    if 7.0 <= z <= 8.0:
        print("it is breakfast time")
    elif 12.0 < z <= 13.0:
        print("it is lunch time")
    elif 18.0 < z <= 19.0:
        print("it is dinner time")
    else:
        print("it is not time to eat")
    return z


def main():
    time = input("What is the time? ")
    time = convert(time)


if __name__ == "__main__":
    main()
