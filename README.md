# Object oriented project with the Tron game

This Thron game was designed from the object oriented concept. There are 4 options to play this Tron game with the following:  
>1. Two human players play take turn 
>2. Two human players move simultaneously 
>3. A human player and a computer player play take turn 
>4. A human player and a smart Computer player play take turn  

Before starting to play a game, the implement in each file asks the user that "Are you ready?". If the user says "yes", it continues to process the play game whereas if the user input "no", the game do not continue the process to play.

---

# Each scenario

## 1. Two human players play take turn

This scenario is contained in [two-player folder](https://github.com/Gracepicharporn/object-oriented-Tron-game/tree/main/two-players). It requireds player_human.py and player_human_implemented.py to implement this game. This game asks the two human players to play take turn on the grid board. Every step of players moving, they will leave the trail on this space and act as a wall. When one player hit the wall, go out of the grid board, hit another player the game will be over. 

## 2. Two human players move simultaneously

In this part, it is provided in the [move-simultaneously folder](https://github.com/Gracepicharporn/object-oriented-Tron-game/tree/main/move-simultaneously). This part was designed that the two-player move simultaneously and the game will end when two players are on a collision path.

## 3. A human player and a computer player play take turn

In this case, it can find in the [player-computer folder](https://github.com/Gracepicharporn/object-oriented-Tron-game/tree/main/player-computer). There are a human player and a computer player in this game. But, the computer is still stupid. They play take turn on the grid board. The human player will start to choose the direction first. The rule for this game is the same as two-player moving simultaneously. 

## 4. A human player and a smart Computer player play take turn

In this case, it is contained in [player-smartcomputer folder](https://github.com/Gracepicharporn/object-oriented-Tron-game/tree/main/player-smartcomputer). This case improves from human and stupid computer play together. They still play take turn and end game when hit the wall, another player, go out of the grid board and on the collision path. However, in this case, the computer is smarter to find the right way for movement.

