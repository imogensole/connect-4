class Connect4Board:
    def __init__(self, rows=6, cols=7):
        self.players = {}
        self.rows = rows
        self.cols = cols
        self.board = [['O' for _ in range(cols)] for _ in range(rows)]
        self.current_player = 1
        self.game_over = False
        self.winner = None

    def print_board(self):
        for row in self.board:
            print('|', end='')
            for cell in row:
                print(cell, end='|')
            print()
        
        print('-' * (2 * self.cols + 1))
    
    def check_valid_symbol(self, symbol, other_symbol = None):
        if symbol == 'O' or symbol == 'o':
            print("Symbol cannot be O, thats the default symbol!")
            return False
        if symbol == other_symbol:
            print("Symbol cannot be the same as the other player's symbol!")
            return False
        if len(symbol) > 1:
            print("Symbol cannot be more than 1 character!")
            return False
        else:
            return True
    
    def set_up_players(self, player_number, other_symbol = None):
        print(f"Enter the name of player {player_number}:")
        player_name = input()
        print(f"Hello {player_name}, what symbol do you want to use?")
        symbol = input()
        while not self.check_valid_symbol(symbol, other_symbol):
            symbol = input()
        self.players[player_number] = {'name': player_name, 'symbol': symbol}
    
    def check_for_winner(self):
        # check for 4 in a row
        for row in self.board:
            for i in range(len(row) - 3):
                if row[i] == row[i+1] == row[i+2] == row[i+3] != 'O':
                    self.game_over = True
                    self.winner = self.players[self.current_player]['name']
                    return
        # check for 4 in a column
        for col in range(self.cols):
            for i in range(self.rows - 3):
                if self.board[i][col] == self.board[i+1][col] == self.board[i+2][col] == self.board[i+3][col] != 'O':
                    self.game_over = True
                    self.winner = self.players[self.current_player]['name']
                    return
        # check for 4 in a diagonal
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != 'O':
                    self.game_over = True
                    self.winner = self.players[self.current_player]['name']                    
                
    def make_move(self):
        print(f"Player {self.current_player} is making a move...")
        print(f"Enter the column number (1-{self.cols}):")
        col = int(input()) - 1
        while col < 0 or col >= self.cols:
            print("Invalid column number. Please enter a valid column number.")
            col = int(input()) - 1
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == 'O':
                self.board[row][col] = self.players[self.current_player]['symbol']
                break
        self.check_for_winner()
        self.current_player = (self.current_player % 2) + 1
        self.print_board()

    def play_game(self):
        print("Welcome to Connect 4!")
        self.set_up_players(1)
        self.set_up_players(2, self.players[1]['symbol'])
        self.print_board()
        while not self.game_over:
            self.make_move()
        print(f"Game over! {self.winner} wins!")