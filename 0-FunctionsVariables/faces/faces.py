def main():
    faces = input("Write a sentence: ")
    faces = convert(faces)
    print(faces)


def convert(faces):
    faces = faces.replace(":)", "🙂").replace(":(", "🙁")
    return faces


main()
