import random

'''
1 for snake
-1 for water
0 for gun
'''

# Generate computer choice
computer = random.choice([-1, 0, 1])

# Map user inputs to numeric values and vice versa
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get user input with validation
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]
    
    # Display choices
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    # Determine winner
    if computer == you:
        print("It's a draw!")
    else:
        if (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            print("You win!")
        else:
            print("You lose!")
