while True:
    try:
        num = input(
            """
            1. open
            2. open
            3. open
            4. open
            (choose one)
            """
        )
        if num == "1":
            print("blah. blah")
        elif num == "2":
            print("bleep")
        elif num == "3":
            print("blah")
        elif num == "4":
            print("bloop")
        else:
            print("not a choice")
    except EOFError:
        break
