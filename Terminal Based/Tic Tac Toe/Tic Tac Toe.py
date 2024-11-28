import numpy as np
import random
def print_board(board):
    for index in range(board.shape[0]) :
        if index != 0 :
            print()
        for index1 in range(board.shape[1]) :
            if index1 != board.shape[1]-1 :
                if board[index][index1] == 0 :
                    print("     ", end = "|")
                elif board[index][index1] >= 1 :
                    print("  X  ", end = "|")
                else : 
                    print("  O  ", end = "|")
            else :
                if board[index][index1] == 0 :
                    print("     ")
                elif board[index][index1] >= 1 :
                    print("  X  ")
                else : 
                    print("  O  ")
        if index != board.shape[0]-1 :
            print("_________________")
    print()
def checker(board) :
    if board[0][0]+board[0][1]+board[0][2] == 3 or board[1][0]+board[1][1]+board[1][2] == 3 or board[2][0]+board[2][1]+board[2][2] == 3 or board[0][0]+board[1][1]+board[2][2] == 3 or board[0][2]+board[1][1]+board[2][0] == 3 or board[0][0]+board[1][0]+board[2][0] == 3 or board[0][1]+board[1][1]+board[2][1] == 3 or board[0][2]+board[1][2]+board[2][2] == 3 :
        return True
    elif board[0][0]+board[0][1]+board[0][2] == -3 or board[1][0]+board[1][1]+board[1][2] == -3 or board[2][0]+board[2][1]+board[2][2] == -3 or board[0][0]+board[1][1]+board[2][2] == -3 or board[0][2]+board[1][1]+board[2][0] == -3 or board[0][0]+board[1][0]+board[2][0] == -3 or board[0][1]+board[1][1]+board[2][1] == -3 or board[0][2]+board[1][2]+board[2][2] == -3 :
        return True
    else :
        return False
class Game :
    def __init__(self) :
        print("=========== WELCOME TO THE GAME ===========")
        self.player_01 = input("Register your name, Player 01: ")
        print(f"WELCOME {self.player_01}, Your symbol is 'X'")
        self.player_02 = input("Register your name, Player 02: ")
        print(f"WELCOME {self.player_02}, Your symbol is 'O'")
        self.board = None
        self.tic_tac_toe_guide()
        self.x = 0
    def tic_tac_toe_guide(self) :
        print()
        print("     General Instructions:\n===============================\n1. The board is a 3 X 3 grid\n2. You will give input based on the index of the board.")
        print("3. For your help the index of the matrix in given down here ↓↓")
        print(f"          x, y\n          ↓  ↓\n         {0,0} | {0,1} | {0,2}\n         {1,0} | {1,1} | {1,2}\n         {2,0} | {2,1} | {2,2}")
        print("4. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins")
        print("5. If the grid is filled without a player getting three marks in a row, the game ends in a tie")
        print() 
        print("                BEST OF LUCK")
        print()
        self.tic_tac_toe()
    def tic_tac_toe(self) :
        self.board = np.zeros((3,3), dtype=int)
        self.x = random.choice([1,2])
        if self.x == 1 :
            print(f"The first one to move is {self.player_01}")
        else :
            print(f"The first one to move is {self.player_02}")
        flag = True
        for index in range(3) :
            for index1 in range(3) :
                x = int(input("Input the X cordinate: "))
                y = int(input("Input the Y cordinate: "))
                if self.x == 1 :
                        self.board[x][y] = 1
                else :
                        self.board[x][y] = -1
                
                print()
                print_board(self.board)
                if checker(self.board) :
                     flag = False
                     if self.x == 1 :
                          print(f"{self.player_01} is the winner.")
                     else :
                          print(f"{self.player_02} is the winner.")
                     break
                if self.x == 2 :
                     self.x = 1 
                else :
                     self.x = 2
            if flag == False:
                 break
        if flag:
             print("This game is a tie") 
        if input(f"Wanna Play another round? 'Yes / No': ") == "Yes" :
            self.tic_tac_toe()
        else :
            return
 
x = Game()
