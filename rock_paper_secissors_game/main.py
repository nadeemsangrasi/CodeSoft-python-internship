import inquirer
import random
print("*"*40)
print("welcome to Rock,Paper,Scissors game")
print("Choose rounds \nwinner score increased by 10\nfinal result will be show after rounds completion")
print("*"*40)
def play_game():
    player_score=0
    computer_score=0
    loop_value=0
    round=inquirer.prompt([inquirer.Text("round",message="Enter how much round do you want to play")])
    if round["round"].isdigit() and not len(round["round"])==0:
        while loop_value<int(round["round"]):
                player_choice = inquirer.prompt([inquirer.List("choice",message="Choose any one of given",choices=["Rock","Paper","Scissors"])])
                computer_choices=["Rock","Paper","Scissors"]
                randomIndex = random.randint(0,len(computer_choices)-1)
                computer_choice=computer_choices[randomIndex]
                if player_choice["choice"]=="Rock" and computer_choice=="Scissors" or player_choice["choice"]=="Scissors" and computer_choice=="Paper" or player_choice["choice"]=="Paper" and computer_choice=="Rock":
                    player_score+=10
                    print("*"*40)
                    print("Player win this round")
                    print("Player score increased by 10")
                    print( "player choice : "+player_choice["choice"])
                    print("computer choice : "+computer_choice)
                    print("*"*40)
                
                elif player_choice["choice"]==computer_choice:
                    print("*"*40)
                    print("Both answer are same round tie")
                    print( "player choice : "+player_choice["choice"])
                    print("computer choice : "+computer_choice)
                    print("*"*40)
                else:
                    computer_score+=10
                    print("*"*40)
                    print("computer win this round")
                    print("computer score increased by 10")
                    print( "player choice : "+player_choice["choice"])
                    print("computer choice : "+computer_choice)
                    print("*"*40)
                loop_value+=1
        if player_score>computer_score:
            print("# "*20)
            print("player win the game")
            print(f"player score :  {player_score}") 
            print(f"computer score : {computer_score}") 
            print("# "*20)
        elif computer_score>player_score:
            print("# "*20)
            print("computer win the game")
            print(f"player score :  {player_score}") 
            print(f"computer score : {computer_score}") 
            print("# "*20)
        else:
            print("# "*20)
            print("Game tie both have equal score")
            print(f"player score :  {player_score}") 
            print(f"computer score : {computer_score}") 
            print("# "*20)
        play_again = inquirer.prompt([inquirer.Confirm('play_again', message="Do you want to a play again?")])
        if play_again["play_again"]:
            play_game()
    else:
        print("Please enter valid rounds")

play_game()
