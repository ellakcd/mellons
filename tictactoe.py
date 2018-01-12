class Player(object):
    def __init__(self, game_piece, name):
        self.game_piece = game_piece
        self.name = name


class Move(object):
    def __init__(self, author, position):
        self.author = author
        self.position = position


class Board(object):
    def __init__(self, moves=[]):
        self.moves = moves

    def display(self):
        print 'player', self.moves[0][0]
        print 'moves', self.moves[0][1]


    def add_move(self, move):
        self.moves.append(move)


class Game(object):
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.active = True
        self.winner = None


harry = Player('Harry', 'X')
hermione = Player('hermione', 'O')

my_board = Board()

my_game = Game(my_board, harry, hermione)

first_move = (harry, [0, 2])
second_move = (harry, [1, 2])

my_board.add_move(first_move)
my_board.display()

#my_board.add_move(second_move)
# board.display()

print my_board.moves