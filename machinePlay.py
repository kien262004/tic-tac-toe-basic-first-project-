from copy import copy

class move():
    def __init__(self, row = 3, col = 3):
        self.row = row
        self.col = col

class board():
    def __init__(self):
        self.move_done = 0 # number of moves had done
        self.square = [[0,0,0],[0,0,0],[0,0,0]] # the board of the game

    # copy the binaray tree
    def operator (self,origin):
        for i in range(3):
            for j in range(3):
                self.square[i][j] = origin.square[i][j]
        self.move_done = origin.move_done
    
    # check the winner  
    def _the_winner(self):
        for i in range(3):
            if self.square[i][0]!=0 and self.square[i][0] == self.square[i][1] and self.square[i][0] == self.square[i][2]:
                return self.square[i][0]
        for i in range(3):
            if self.square[0][i]!=0 and self.square[0][i] == self.square[1][i] and self.square[0][i] == self.square[2][i]:
                return self.square[0][i]
        if self.square[0][0]!=0 and self.square[1][1] == self.square[0][0] and self.square[0][0] == self.square[2][2]:
                return self.square[0][0]
        if self.square[0][2]!=0 and self.square[1][1] == self.square[0][2] and self.square[1][1] == self.square[2][0]:
                return self.square[2][0]
        return 0
    
    # the end of the games
    def done(self):
        return (self.move_done == 9 or self._the_winner() > 0)
    
    # the play turn
    def play(self, try_it):
        self.square[try_it.row][try_it.col] = self.move_done%2 + 1
        self.move_done += 1
    
    # evaluate the value of the location
    def evaluate(self):
        winner = self._the_winner()
        if winner == 1:
            return 10 - self.move_done
        elif winner == 2:
            return -10 + self.move_done
        return 0
    
    # create the list of legal moves
    def legal_moves(self, moves):
        count = 0
        if len(moves) >0:
            moves.clear()
        for i in range(3): 
            for j in range(3):
                if self.square[i][j] == 0:
                    moves.append(move(i,j))
                    count +=1
        return count
    
    # the worst case if each turn
    def worst_case(self):
        if (self.move_done % 2 == 0):
            return -10
        return 10
    
    # the beter value
    def better(self, value, old_value):
        if (self.move_done % 2 == 0):
            if value > old_value:
                return True
            return False
        else:
            if value < old_value:
                return True
            return False
    
    # display the game
    def print_game(self):
        for i in range(3):
            for j in range(3):
                print(self.square[i][j], end=" ")
            print()
        print()
        
    # clear the squares
    def clear(self):
        self.move_done = 0
        for i in range(3):
            for j in range(3):
                self.square[i][j] = 0
    
# function looking the next turn
def look_ahead(game = board(), depth = 0, recommended = move()):
    if game.done() or depth == 0:
        return game.evaluate()
    else:
        moves = list()
        game.legal_moves(moves)
        best_value = game.worst_case()
        while (len(moves) != 0):
            try_it = moves[-1]
            reply = move()
            new_game = board()
            new_game.operator(game)
            new_game.play(copy(try_it))
            value = look_ahead(new_game, depth - 1, reply)
            if (game.better(value,best_value)):
                best_value = value
                recommended.row = try_it.row
                recommended.col = try_it.col
            moves.pop(-1)
        return best_value

recommend = move() # varible to storages the move
