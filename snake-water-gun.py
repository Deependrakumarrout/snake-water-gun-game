#snake water gun - (read the instruction before playing this game...)
#if i will get snake and computer will get water then snake will drink water so i will win that game.
#if i will get gun and computer will get snake then i will win because i can kill that snake by gun.
#if i will make gun and computer will make water then i will lose because that gun will goes deep into the water.

#so here we will use the random.choise function to choose one the option
#It will say what you want to do snake water gun: in shot you will type s,w,g
#Then it will show who won the match
#That will run 10 time so put on while loop
#Then when game over it will congress the winner
#And it will also show the list of how much time i win and computer win
#And i also put a restart option in this game.

def restart():
    computer_score=0
    human_score=0
    tie=0
    m=1
    print()
    print("Let's play snake water and gun")
    print("Loading...")
    while m<=10:
        print()
        print("Attempt number",m)
        print("Press s for snake")
        print("Press w for water")
        print("Press g for gun")
        choose=("snake","water","gun")

        man=input("Enter here:")
        import random
        choose = random.choice(choose)
        if man=="s".lower():
            computer = choose
            print()
            print("You have selected: snake")
            print(f"computer have selected: {computer}")
            if man=="s".lower() and computer=="gun":
                print("Computer has win this match")
                computer_score=computer_score+1
                print("computer score",computer_score)
            elif man=="s".lower() and computer=="water":
                print("You will win the match")
                human_score = human_score + 1
                print("human score", human_score)
            else:
                print("Match tie")
                tie = tie + 1
                print("counting tie", tie)

        elif man=="w":
            computer=choose
            print()
            print("You have selected water")
            print(f"computer have selected: {computer}")
            if man=="w".lower() and computer=="gun":
                print("You have won this match")
                human_score = human_score + 1
                print("human score", human_score)

            elif man=="w".lower() and computer=="snake":
                print("Computer have won this match")
                computer_score = computer_score + 1
                print("computer score", computer_score)

            else:
                print("Match tie")
                tie = tie + 1
                print("counting tie", tie)

        elif man=="g":
            computer=choose
            print()
            print("you have selected: gun")
            print(f"Computer have selected: {computer}")
            if man=="g".lower() and computer=="snake":
                print("You have won this match")
                human_score = human_score + 1
                print("human score", human_score)

            elif man=="g".lower() and computer=="water":
                print("Computer have won this match")
                computer_score = computer_score + 1
                print("computer score", computer_score)

            else:
                print("Match tie")
                tie = tie + 1
                print("counting tie", tie)


        else:
            print("Invalid input please enter from the given list..")

        m+=1
    print()
    print("Total human score is:",human_score)
    print("Total Computer score is:",computer_score)
    print("Total Tie is:",tie)
    if computer_score > human_score:
        print("computer WON!!!!")
    elif computer_score == human_score:
        print("TIE")
    else:
        print("human WON!!!!")
    print()
    print("Do you want to restart:")
    again=input("Press y for yes n for no:")
    if again =="y".lower():
        restart()
    else:
        print("Ok player don't want to restart this game")
restart()



