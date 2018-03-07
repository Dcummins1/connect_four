import pprint as pp
from itertools import cycle

class play_game():
    """creates the matrix and performs actions on that matrix"""
    def __init__(self): #2darray size
        self.board = [[0] *7 for _ in range(6)] #0 for empty, 1 for player 1, 2 for player 2



    def display(self):
        """display the board using pprint"""
        pp.pprint(self.board)

    def move(self, player, move):  # player number, position of top row to play into
        i = 0
        if self.board[0][move] == 0:
            while i < 6:
                if self.board[i][move] == 0:
                    i += 1
                else:
                    break
            self.board[i - 1][move] = player
            if self.check_surrounds(player, i-1, move):
                    return True
        else:
            move1 = int(input('invalid move enter again'))
            self.move(player, move1-1)




    def check_square(self, player, x, y): # check if square belongs to player
        if ((y < 0) or (x < 0) or (y >= 7 or x >= 6)):
            return False
        else:
            if self.board[x][y] == player:
                return True
            else:
                return False

    def check_surrounds(self, player, x, y):
        check_win = {'horizontal': [(0, -1), (0, +1)], 'vertical': [(+1, 0), (-1, 0)],
                      'diag_one': [(+1, +1), (-1, -1)], 'diag_two': [(+1, -1), (-1, +1)]}
        for i in check_win:
            start_x1 = x
            start_y1 = y
            start_x = x
            start_y = y
            up = True  # up for vertical right, for horizontal/diagonal
            down = True # down for vertical, left for horizontal/diagonal
            count_up = 0
            count_down = 0
            total = 1
            while up == True:
                if self.check_square(player, start_x1 + check_win[i][0][0] , start_y1 + check_win[i][0][1]):
                    count_up += 1
                    start_x1 = start_x1 + check_win[i][0][0]
                    start_y1 = start_y1 + check_win[i][0][1]
                else:
                    up = False
            while down == True:
                if self.check_square(player, start_x + check_win[i][1][0], start_y + check_win[i][1][1]):
                    count_down += 1
                    start_x = start_x + check_win[i][1][0]
                    start_y = start_y + check_win[i][1][1]
                else:
                    down = False

            total += count_down + count_up
            if total == 4:
                print("Player %d wins!!!!!!!!!!"  % (player))
                return True


    def play(self, player, user_input):
        action = user_input - 1
        if self.move(player, action):
            self.display()
            return True


def main():
    board = play_game()
    board.display()
    for player in cycle([1, 2]):
        while True:
            try:
                player_move = int(input("Player %d Enter the row to drop your piece (1-7)" % (player)))
                if check_inp(player_move):
                    break
                else:
                    print("Please enter a valid number from 1-7")
            except ValueError:
                print("Please enter a valid number from 1-7")
        if board.play(player, player_move):
            return True
        board.display()





def check_inp(x):
    return isinstance(x, int) and 0 < x < 8





if __name__=="__main__":
    main()


#
#print(board.check_square(1, 5, 6))
# board = play_game()
# board.move(1,0)
# board.move(2,1)
# board.move(1,2)
# board.move(1,3)
# board.move(1,1)
# board.move(1,2)
# board.move(2,3)
# board.move(1,2)
# board.move(1,3)
# board.display()
# board.move(1,3)
# board.display()



# board.move(1, 6)
# board.display()
# board.move(1, 6)
# board.display()
# board.move(1, 6)
# board.display()
# board.move(1, 6)
# board.display()
# board.move(2, 5)
# board.display()
# board.move(2, 4)
# board.display()
# board.move(2, 3)
# board.display()
# board.move(2, 2)
# board.display()







