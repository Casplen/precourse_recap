guess= input("Rock, Paper, Scissors! Your play? ")
print("I play rock.")
if guess == "rock":
    print("Draw!")
elif guess == "paper":
    print("Paper beats rock. You win!")
elif guess == "scissors":
    print("Rock beats scissors. You lose!")
else:
    print("Invalid- enter rock, paper or scissors.")
