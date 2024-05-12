import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit

elif len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit

elif not (sys.argv[1]).endswith(".csv"):
    print("Not a csv file")
    sys.exit

else:
    data = []
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                data.append(line.strip().split(","))
    except FileNotFoundError:
        print("file does not exist")

    print(
        tabulate(
            data,
            headers="firstrow",
            tablefmt="grid",
        )
    )
