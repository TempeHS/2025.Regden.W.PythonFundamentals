import random


def ask_question():
    score = 0
    for _ in range(10):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        z = x + y
        rng = 0
        while rng < 3:
            try:
                print("What does", x, "+", y, "equal? ")
                user_answer = int(input(""))
                if user_answer == z:
                    print("Good job!")
                    score += 1
                    break
                if user_answer != z:
                    print("EEE")
                    rng += 1
                if rng == 3:
                    print((x), "+", (y), "=", (z))
            except ValueError:
                print("Invalid answer")
    return score


def main():
    while True:
        level_choice = input(
            """
Choose a level:
1. Level 1
2. Level 2
3. Level 3
4. Exit
(choose one): """
        )

        if level_choice in ["1", "2", "3"]:
            score = ask_question()
            print("your score is:", score)
            break

        elif level_choice == "4":
            print("No worries")
            break
        else:
            continue


if __name__ == "__main__":
    main()
