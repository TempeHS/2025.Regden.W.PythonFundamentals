def main():
    glist = {}
    try:
        while True:
            list = input("Enter a grocery item ").strip().title()
            if list:
                glist[list] = glist.get(list, 0) + 1
    except EOFError:
        pass

    sort_glist = sorted(glist.keys(), key=str.upper)

    for list in sort_glist:
        count = glist[list]
        print("\n" f"{count}, {list.upper()}", end="\n")


main()
