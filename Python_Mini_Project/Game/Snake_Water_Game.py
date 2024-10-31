import random

def play_game():
    youDict = {"snake": 1, "water": -1, "gun": 0}
    reverseDict = {1: "snake", -1: "water", 0: "gun"}
    
    while True:
        youstr = input("Enter your choice (or 'q' to quit): ")
        if youstr.lower() == 'q':
            print("Game ended. Thanks for playing!")
            break

        if youstr not in youDict:
            print("Invalid choice. Please choose 'snake', 'water', or 'gun'.")
            continue

        you = youDict[youstr]
        computer = random.choice([-1, 0, 1])
        
        print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
        
        if computer == you:
            print("It's a draw.")
        else:
            if (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
                print("You Win!")
            else:
                print("You Lose!")

if __name__ == '__main__':
    play_game()
