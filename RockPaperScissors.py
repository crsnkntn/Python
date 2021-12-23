import random

options = ["Rock", "Paper", "Scissors"]

# 0 => a wins, 1 => b wins, 2 => tie
def rules(a, b): 
    print(a, "  vs.  ", b)
    if a == b:
        return 2
    elif a == "Rock" and b == "Paper":
        return 1
    elif a == "Paper" and b == "Rock":
        return 0
    elif a == "Rock" and b == "Scissors":
        return 0
    elif a == "Scissors" and b == "Rock":
        return 1
    elif a == "Paper" and b == "Scissors":
        return 1
    elif a == "Scissors" and b == "Paper":
        return 0
    else:
        return 2 


def rockpaperscissors():
    player_wins, rounds = 0, 0
    player, chaos = "Rock", "Paper"
    while player in options:
        player = input("Rock, Paper, or Scissors?\n")
        chaos = options[random.randint(0, 2)]
        result = rules(player, chaos)
        if result == 0:
            player_wins += 1
        rounds += 1
        print("Player Win %    ", (player_wins / rounds) * 100)
    print("Final Player Win %:    ", (player_wins / rounds) * 100)



if __name__ == "__main__":
    rockpaperscissors()