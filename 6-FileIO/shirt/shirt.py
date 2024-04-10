from PIL import Image
import sys

try:
    file, type = sys.argv[1].split(".")
    if not (sys.argv[1]).endswith((".jpg", ".jpeg", ".png")):
        print("Not the right type of file")
        sys.exit

    if not (sys.argv[2]).endswith(type):
        print("Not the same type of file")
        sys.exit
except IndexError:
    print("Too few arguments")
    sys.exit()

if len(sys.argv) > 3:
    print("Too many arguments")
    sys.exit

try:
    with Image.open(sys.argv[1]) as jpgfile:
        with Image.open("shirt.png") as shirt:
            nshirt = shirt.resize((1130, 1100))
            njpgfile = jpgfile.crop((0, 0, 1200, 1400))
            njpgfile.paste(nshirt, (55, 300), nshirt)
            njpgfile.save(sys.argv[2])
            print("done")
except FileNotFoundError:
    print("file does not exist")
