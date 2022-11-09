#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 22:16:35 2022

@author: gracepichar
"""

from Part1_human_smartcomputer import Board, Player1, Humanplayer, Computerplayer, SmartCompuer  
#create the welcome massage befor playing
print("Weclome to the Trone Grame!")
print("Are you ready?")
#asking user that they are ready for playing this game
#yes means play
#no means not ready to play
answer = input("Enter yes/no : ") 


if answer == "yes": #if they say yes, we will play this game

    #create the instruction for this game
    print("Great!. Let's start!")
    print("Before we will start you need to know about our rules.")
    print("Please read the instruction be carefully.")
    print("----------------------------------------------------------------------------")
    print("The rule of this game.")
    print("1. This games have two players; 1 is player1 and 2 is player2.\n The player1 = Human Player is you!!\n Player2 = The Smart Computer player")
    print("They take turns in moving on  a grid board")
    print("2. The players can move in four direcion.")
    print("\t Up : U")
    print("\t Down : D")
    print("\t Left : L")
    print("\t Right : R")
    print("5. After the player moves, it will leaves a trail on the space and it acts as a wall.")
    print("6. The game will be over, if one player crashes into the wall or move the wrong direction and they crash on the path.")
    print("----------------------------------------------------------------------------")
    print("Have fun!")


    if __name__=='__main__':
        
        play_again = True #to check the user want to play game again afer gam over:
        
        while play_again: #check the condition for playong game again
            try: #check if user input number for board size
                size = int(input("Enter the board size: "))
                if size >= 4: #the board size should more than 4
                    x = Board(size)
                    name_player = []
                    id_player = []
                    name_player1 = input("Hello! Player1. Please enter you name: ")
                    try: #check the use input the number for ID player.
                        id_player1 = int(input("Enter your ID: "))
                        name_player.append(name_player1)#append in player name list
                        id_player.append(id_player1) #add to id player list
                        p1 = Humanplayer(name_player1, id_player1,"","",size)
                        name_player2 = input("Hi!, please give the name of Smart Computer Player: ")
                        
                        while True: #check  if user input the repeating name and ID 
                            if  name_player2 in name_player: #check repeating name
                                print("Game over!, the name player was repeated with player1")
                                break #beak loop to ask user play game again
                            id_player2 = int(input("Enter your ID: "))
                            if  id_player2 in id_player: #check repeating id
                                print("Game over!, the id player was repeated with player1")
                                break #beak loop to ask user play game again
                        
                            p2 = SmartCompuer("","",name_player2, id_player2,size)
                            print("In this game. There are two player")
                            p2.info_player1()
                            p2.position_player2()
                            print("Your board was created!. The size is " + str(size)+" * " + str(size))
                            print("The two player had already placed in this board")
                            p2.size_board()
                            play = x.check_game()
                            print("Let's start!")
                            while play: #ask two to enter the two player movement
                                p1.move_player1()
                                p1.size_board()
                                play=x.check_game()
                                if play == False: #if game over, the loop for entering movement will break out.
                                    break
                                p2.get_move()#random movement for computer player
                                p2.check_move()#check random movemt
                                p2.move_player2()
                                p2.size_board()
                                play=x.check_game()
                                if play == False: #if game over, the loop for entering movement will break out.
                                    break
                            break #after game over to ask user play again
                            
                     #if user input invalid number for ID player.
                    except ValueError:
                        print("Game over!, please input the number for ID only.")
                    except:
                        print("Game over!, please input the number for ID only.")
                
                else: #when the board is below 4
                    print("Sorry, game over the board size should be more than 4")
                
            except ValueError: #check if user doesn't input valid number for board size
                print("Gameover!. please input the number only for board size.")
            except: #if somthing went worong
                print("Gameover!. please input the number only for board size.")
            
            print("Do you want to play this game again?")   
            ask_again = input("Enter y/n: ") #ask user to play game again
            if ask_again == "y": #if the user enter "y", it will run the loop for play again
                play_again = True
            
            else: #if the user enter "n", it will not run the loop for play again
                print("Thank you. See you later")
                play_again = False
                
elif answer  == "no": #if they say no, we will not continue to play the game
    print("Oh, I am sorry. If you have a free time. Let's come back and play together!")
    

else:  #if user enter other word
    print("Sorry, I don't understand. Could you please type yes/no only?")

      
    
            
