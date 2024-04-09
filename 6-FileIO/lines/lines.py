import sys

# counts lines
# command line asks for one file
# get file
# remove whitesapce, and comments
if len(sys.argv) < 2:
    print("Too few arguments")
    sys.exit


if len(sys.argv) > 2:
    print("Too many arguments")
    sys.exit

elif not sys.argv[1].endswith(".py"):
    print("Not a python file")
    sys.exit

else:
    try:
        linec = 0
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                linec += 1
            print(linec)
    except FileNotFoundError:
        print("file does not exist")
