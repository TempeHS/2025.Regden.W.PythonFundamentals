import csv
import sys

if len(sys.argv) < 3:
    print("Too few arguments")
    sys.exit


elif len(sys.argv) > 3:
    print("Too many arguments")
    sys.exit

elif not (sys.argv[1]).endswith(".csv") or not (sys.argv[2]).endswith(".csv"):
    print("Not a csv file")
    sys.exit

data = []
try:
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        if "name" not in reader.fieldnames or "house" not in reader.fieldnames:
            print("Input CSV file must have 'name' and 'house' columns.")
            sys.exit(1)
        new = ["first", "last", "house"]

        with open((sys.argv[2]), "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=new)
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split()
                writer.writerow({"last": last, "first": first, "house": row["house"]})

except FileNotFoundError:
    print("file does not exist")
