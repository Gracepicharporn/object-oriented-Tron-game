#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 21:28:39 2021

@author: gracepichar
"""
import random 
# define the class for board including the boaed template, position of player1 and player2 when the game start
class Board:
    play = ""
    template = ""
    # define the Board game size
    def __init__(self,size,*args,**kwargs):
        self.size = size
        
        self.row = ['#'] + [i for l in [" ", "|"] * (self.size-1) for i in l] + [" "] +["#"] #create the row of board game
        Board.template = [self.row[:] for i in range(1,self.size+1)]#create the 2D-array board game
        Board.play = True #check the condition in this game
        
        
    def size_board(self):  # generate and print the board for playing   
        print("#" * (self.size*2))
        for a in Board.template:
            print("".join(a))
        print("#" * (self.size*2))
    
    def check_game(self): #check the loop for end game
        return Board.play
    
       
#define the class for player1      
class Player1(Board):
    
    #define the name and id of player1
    def __init__(self,name1,id1,name2,id2,size,*args,**kwargs):
        super().__init__(size,*args,**kwargs)
        self.name1 = name1
        self.id1 = id1
        self.player1X = 0 #setting deflut location in row of player1
        self.player1Y = 1 #setting deflut location in rcolum of player1
        self.direction1 = ""
        self.position1 = []
        self.name2 = name2
        self.id2 = id2
        self.player2X = self.size -1 #setting deflut location in row of computerplayer
        self.player2Y = (self.size*2)-1 #setting deflut location in colum of computerplayer

        
    #print the player1 and computerplayer information
    def info_player1(self):
        print("Player 1: " +  self.name1 + " ID: " + str(self.id1))
        print("Computer Player: " +  self.name2 + " ID: " + str(self.id2))
    
    
    #place the player1 and computerplayer on the grid board
    def position_player2(self): #place the player1 in the board
        Board.template[self.player1X][self.player1Y] = "1" #placed player1 in on the top at the left corner
        Board.template[self.player2X][self.player2Y] = "2" #placed computerplayer in on the bottom at the right corner
        self.position1.append((self.player1X,self.player1Y))
        return Board.template
       
    
    #create the movement of player1
    def move_player1(self):
        self.direction1 = input("Enter the move for player1: ") #input the direction of player1
        if self.direction1 == "U": #move up
           
           self.player1X -= 1
           if self.player1X >= 0: #check the diection player1 isn't out of board from the top
               
               if Board.template[self.player1X][self.player1Y] == " ": #check the next position is emphty
                   Board.template[self.player1X][self.player1Y] = "1"
                   Board.template[self.player1X+1][self.player1Y] = "X"
                   self.position1.append((self.player1X,self.player1Y))
               elif Board.template[self.player1X][self.player1Y] == "2": #check if player one and two are on the collsion path
                    print("Game over!!!. Player1 and Computerplayer are on the collsion path")
                    print("No one win this game!!")
                    Board.template[self.player1X+1][self.player1Y] == "1"
                    Board.play = False
               else: # game ove if the player1 hit the wall 
                   print("Game over, player 1 hit the wall")
                   print("The winner is Computerplayer!!")
                   Board.template[self.player1X+1][self.player1Y] = "X"
                   Board.play = False
                   
           else: #game over if the player1 move out of the board from the top
               print("Game over!!!")
               print("The player1 go outside the board from the top")
               print("The winner is Computerplayer!!")
               Board.template[self.player1X+1][self.player1Y] = "X"
               Board.template[self.player1X][self.player1Y] == " "
               Board.play = False
               
           return Board.play
           
        elif self.direction1 == "D": #move down
            
            self.player1X += 1
            if self.player1X <= (self.size-1): #check the diection player1 isn't out of board from the bottom
            
                if Board.template[self.player1X][self.player1Y] == " ": #check the next position is emphty
                    Board.template[self.player1X][self.player1Y] = "1"
                    Board.template[self.player1X-1][self.player1Y] = "X"
                    self.position1.append((self.player1X,self.player1Y))
                elif Board.template[self.player1X][self.player1Y] == "2": #check if player one and two are on the collsion path
                    print("Game over!!!. Player1 and Computerplayer are on the collsion path")
                    print("No one win this game!!")
                    Board.template[self.player1X-1][self.player1Y] == "1"
                    Board.play = False
                else: # game ove if the player1 hit the wall 
                    print("Game over, player 1 hit the wall")
                    print("The winner is Computerplayer!!")
                    Board.template[self.player1X-1][self.player1Y] = "X"
                    Board.play = False
                    
            else: #game over if the player1 move out of the board from the bottom
               print("Game over!!!")
               print("The player1 go outside the board from the bottom")
               print("The winner is Computerplayer!!")
               Board.template[self.player1X-1][self.player1Y] = "X"
               Board.play = False
               
            return Board.play
            
        elif self.direction1 == "L": #move left
            
            self.player1Y -= 2
            if 0 <= self.player1Y <= (self.size*2)-1: #check the diection player1 isn't out of board from the left
                
                if Board.template[self.player1X][self.player1Y] == " ": #check the next position is emphty
                    Board.template[self.player1X][self.player1Y] = "1"
                    Board.template[self.player1X][self.player1Y+2] = "X"
                    self.position1.append((self.player1X,self.player1Y))
                elif Board.template[self.player1X][self.player1Y] == "2": #check if player one and two are on the collsion path
                    print("Game over!!!. Player1 and Computerplayer are on the collsion path")
                    print("No one win this game!!")
                    Board.template[self.player1X][self.player1Y+2] == "1"
                    Board.play = False
                else: # game ove if the player1 hit the wall 
                    print("Game over, player 1 hit the wall")
                    print("The winner is Computerplayer!!")
                    Board.template[self.player1X][self.player1Y+2] = "X"
                    Board.play = False
                    
            else: #game over if the player1 move out of the board from the left
               print("Game over!!!")
               print("The player1 go outside the board from the left")
               print("The winner is Computerplayer!!")
               Board.template[self.player1X][self.player1Y+2] = "X"
               Board.play = False    
               
            return Board.play
            
            
        elif self.direction1 == "R": #move right
            
            self.player1Y += 2 #check the diection player1 isn't out of board from the right
            if 0 <= self.player1Y <= (self.size*2)-1: #check the diection player1 isn't out of board from the right
            
                if Board.template[self.player1X][self.player1Y] == " ": #check the next position is emphty
                    Board.template[self.player1X][self.player1Y] = "1"
                    Board.template[self.player1X][self.player1Y-2] = "X"
                    self.position1.append((self.player1X,self.player1Y))
                elif Board.template[self.player1X][self.player1Y] == "2": #check if player one and two are on the collsion path
                    print("Game over!!!. Player1 and Computerplayer are on the collsion path")
                    print("No one win this game!!")
                    Board.template[self.player1X][self.player1Y-2] == "1"
                    Board.play = False
                else: # game ove if the player1 hit the wall 
                    print("Game over, player 1 hit the wall")
                    print("The winner is Computerplayer!!")
                    Board.template[self.player1X][self.player1Y-2] = "X"
                    Board.play = False
                    
            else: #game over if the player1 move out of the board from the left
                 print("Game over!!!")
                 print("The player1 go outside the board from the right")
                 print("The winner is Computerplayer!!")
                 Board.template[self.player1X][self.player1Y-2] = "X"
                 Board.play = False
                 
            return Board.play
            
        else: #if user type the other character
            print("Sorry, please type the U/D/L/R only!")
            print("Game Over!!")
            print("The winner is Computerplayer!!")
            Board.play = False
            return Board.play
        
        return Board.template
    
        
#create the HumanPlayer class   
class Humanplayer(Player1):
    
    def __init__(self,name1,id1,size,*args,**kwargs):
        super().__init__(name1,id1,size,*args,**kwargs)
        
    
#create the Computerplayer class  
class Computerplayer(Player1):
    
    def __init__(self,name2,id2,size,*args,**kwargs):
        super().__init__(name2,id2,size,*args,**kwargs)
        self.move = ""
        self.position2 = []
        
    def get_move(self): #random movement of computerplayer
        self.move = random.randint(1, 4)
        
    def check_firtsstep(self): #check the first movement of computerplayer isn't D and R
        while self.move == 2 or self.move == 4 :
            self.move = random.randint(1, 4)
            
        return self.move
        
    
        #create the movement of computerplayer
    def move_player2(self):
        self.store_move ={ 1:'U', 2:'D' , 3:'L', 4:'R'} #input the direction of computerplayer
        self.direction2 = self.store_move[self.move]
        print("The computer player(Player2) move: " + self.direction2)
        
        if self.direction2 == "U": #go up
           self.player2X -= 1
           if self.player2X >= 0: #check the diection computerplayer isn't out of board from the top
           
               if Board.template[self.player2X][self.player2Y] == " ": #check the next position is emphty
                   Board.template[self.player2X][self.player2Y] = "2"
                   Board.template[self.player2X+1][self.player2Y] = "X"
                   self.position2.append((self.player2X,self.player2Y))
               elif Board.template[self.player2X][self.player2Y] == "1": #check if player one and two are on the collsion path
                    print("Game over!!!. Player1 and Computerplayer are on the collsion path")
                    print("No one win this game!!")
                    Board.template[self.player2X+1][self.player2Y] == "2"
                    Board.play = False
               else: # game ove if the computerplayer hit the wall 
                   print("Game over, Computerplayer hit the wall")
                   print("The winner is Player1!!")
                   Board.template[self.player2X+1][self.player2Y] = "X"
                   Board.play = False
                   
           else: #game over if the computerplayer move out of the board from the top
               print("Game over!!!")
               print("The Computerplayer go outside the board from the top")
               print("The winner is Player1!!")
               Board.template[self.player2X+1][self.player2Y] = "X"
               Board.template[self.player2X][self.player2Y] == " "
               Board.play = False
               
           return Board.play
           
           
        elif self.direction2 == "D": #go down
            self.player2X += 1
            if self.player2X <= (self.size-1): #check the diection computerplayer isn't out of board from the bottom
            
                if Board.template[self.player2X][self.player2Y] == " ": #check the next position is emphty
                    Board.template[self.player2X][self.player2Y] = "2"
                    Board.template[self.player2X-1][self.player2Y] = "X"
                    self.position2.append((self.player2X,self.player2Y))
                elif Board.template[self.player2X][self.player2Y] == "1": #check if player one and two are on the collsion path
                    print("Game over!!!. Player1 and Computerplayer are on the collsion path")
                    print("No one win this game!!")
                    Board.template[self.player2X-1][self.player2Y] == "2"
                    Board.play = False
                else: # game ove if the computerplayer hit the wall 
                    print("Game over, Computerplayer hit the wall")
                    print("The winner is Player1!!")
                    Board.template[self.player2X-1][self.player2Y] = "X"
                    Board.play = False
                    
            else: #game over if the computerplayer move out of the board from the bottom
               print("Game over!!!")
               print("The Computerplayer go outside the board from the bottom")
               print("The winner is Player1!!")
               Board.template[self.player2X-1][self.player2Y] = "X"
               Board.play = False
               
            return Board.play
            
        elif self.direction2 == "L": #move left
           
            self.player2Y -= 2
            if 0 <= self.player2Y <= (self.size*2)-1: #check the diection computerplayer isn't out of board from the left
                
                if Board.template[self.player2X][self.player2Y] == " ": #check the next position is emphty
                    Board.template[self.player2X][self.player2Y] = "2"
                    Board.template[self.player2X][self.player2Y+2] = "X"
                    self.position2.append((self.player2X,self.player2Y))
                elif Board.template[self.player2X][self.player2Y] == "1": #check if player one and two are on the collsion path
                    print("Game over!!!. Player1 and Computerplayer are on the collsion path")
                    print("No one win this game!!")
                    Board.template[self.player2X][self.player2Y+2] == "2"
                    Board.play = False
                else: # game ove if the computerplayer hit the wall 
                    print("Game over, Computerplayer hit the wall")
                    print("The winner is Player1!!")
                    Board.template[self.player2X][self.player2Y+2] = "X"
                    Board.play = False
                    
            else: #game over if the computerplayer move out of the board from the left
               print("Game over!!!")
               print("The Computerplayer go outside the board from the left")
               print("The winner is Player1!!")
               Board.template[self.player2X][self.player2Y+2] = "X"
               Board.play = False    
            
            return Board.play
            
        elif self.direction2 == "R": #move right
            
            self.player2Y += 2 
            if 0 <= self.player2Y <= (self.size*2)-1: #check the diection computerplayer isn't out of board from the right
            
                if Board.template[self.player2X][self.player2Y] == " ": #check the next position is emphty
                    Board.template[self.player2X][self.player2Y] = "2"
                    Board.template[self.player2X][self.player2Y-2] = "X"
                    self.position2.append((self.player2X,self.player2Y))
                elif Board.template[self.player2X][self.player2Y] == "1": #check if player one and two are on the collsion path
                    print("Game over!!!. Player1 and Computerplayer are on the collsion path")
                    print("No one win this game!!")
                    Board.template[self.player2X][self.player2Y-2] == "2"
                    Board.play = False
                else: # game ove if the computerplayer hit the wall 
                    print("Game over, Computerplayer hit the wall")
                    print("The winner is Player1!!")
                    Board.template[self.player2X][self.player2Y-2] = "X"
                    Board.play = False
                    
            else: #game over if the computerplayer move out of the board from the left
                 print("Game over!!!")
                 print("The Computerplayer go outside the board from the right")
                 print("The winner is Player1!!")
                 Board.template[self.player2X][self.player2Y-2] = "X"
                 Board.play = False
                 
            return Board.play
            
        else: #if user type the other character
            print("Sorry, please type the U/D/L/R only!")
            print("Game Over!!")
            print("The winner is Player1!!")
            Board.play = False
            return Board.play
        
        return Board.template
    

    
        
    
    
        
    
