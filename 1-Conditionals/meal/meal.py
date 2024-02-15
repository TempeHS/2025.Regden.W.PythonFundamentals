def convert(time: str):
    hours, minutes = time.split(":")
    x = float(minutes) / 60
    z = float(hours) + x
    return z


def main():
    time = input("What is the time? ")
    y = convert(time)


if 7.0 <= y <= 8.0:
    print("it is breakfast time")
elif 8.0 < y < +9.0:
    print("x is greater than y")
elif 9.0 < y <= 10.0:
    print("x is equal to y")

if __name__ == "__main__":
    main()
