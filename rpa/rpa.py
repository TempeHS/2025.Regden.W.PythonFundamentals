def main():
    player_choice = input("rock, paper or scissors? ")
    if computer_choice() == player_choice:
        print("draw")
    if computer_choice() == "rock" and player_choice == "paper":
        print("win")
    if computer_choice() == "rock" and player_choice == "scissor":
        print("lose")
    if computer_choice() == "scissor" and player_choice == "paper":
        print("win")
    if computer_choice() == "scissor" and player_choice == "rock":
        print("lose")
    if computer_choice() == "paper" and player_choice == "rock":
        print("win")
    if computer_choice() == "paper" and player_choice == "scissor":
        print("lose")


def computer_choice():
    computer_choice = "rock"
    return computer_choice


main()
