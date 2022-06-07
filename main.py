import random
option = ["Rock", "Scissor", "Paper"]
tie = True
while tie:
    player_choice = ""
    while player_choice != "R" and player_choice != "S" and player_choice != "P":
        player_choice = input("pick an option between R, P or S: ")
        if player_choice != "R" and player_choice != "S" and player_choice != "P":
            print("Error\n")
    CPU_choice = random.choice(option)
    if player_choice == "R":
        player_choice = "Rock"
    elif player_choice == "S":
        player_choice = "Scissor"
    else:
        player_choice = "Paper"
    print("Player (", player_choice, ") : CPU (", CPU_choice, ")")
    if player_choice == "Rock" and CPU_choice == "Paper":
        print("CPU wins")
        tie = False
    elif player_choice == "Paper" and CPU_choice == "Scissor":
        print("CPU wins")
        tie = False
    elif player_choice == "Scissor" and CPU_choice == "Rock":
        print("CPU wins")
        tie = False
    elif player_choice == CPU_choice:
        tie = True
    else:
        print("Player wins")
        tie = False
