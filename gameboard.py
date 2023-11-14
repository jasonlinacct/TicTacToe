
class InvalidMoveError(Exception):
    pass


class BoardClass:

    def __init__(self, player_one, player_two, current_player) -> None:
        """
        Initiates the board, contains all the information that the board needs.
        """
        self.player_one = player_one
        self.player_two = player_two
        self.current_player = current_player
        self.last_player_turn = None
        self.num_wins = 0
        self.num_ties = 0
        self.num_losses = 0
        self.total_games_played = 0

        self.board = [[' ', ' ', ' '], 
                      [' ', ' ', ' '], 
                      [' ', ' ', ' ']]

    def print_board(self):
        print(self.board)

    def update_games_played(self) -> None:
        """
        Adds a counter to the total_games_played.
        """
        self.total_games_played += 1

    def reset_game_board(self) -> None:
        """
        Sets the board back to its original state.
        """
        self.board = [[' ', ' ', ' '], 
                      [' ', ' ', ' '], 
                      [' ', ' ', ' ']]

    """     
    def draw_board(self):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            board = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
            rows, columns = 3, 3

            for x in range(rows):
                print('\n+---+---+---+')
                print('|', end='')
                for y in range(columns):
                    print('', board[x][y], end=' |')
                print('\n+---+---+---+') """

    """     
    def update_game_board(self, num, turn):
            num -= 1
            if (num == 0):
                self.board[0][0] = turn
            elif (num == 1):
                self.board[0][1] = turn
            elif (num == 2):
                self.board[0][2] = turn
            elif (num == 3):
                self.board[1][0] = turn
            elif (num == 4):
                self.board[1][1] = turn
            elif (num == 5):
                self.board[1][2] = turn
            elif (num == 6):
                self.board[2][0] = turn
            elif (num == 7):
                self.board[2][1] = turn
            elif (num == 8):
                self.board[2][2] = turn """

    def updateGameBoard(self, row: int, col: int, turn: str) -> None | bool:
        """
        Updates the gameboard given username and row, col with Xs or Os (depends on player one or two.)

        player_name (str): the name of the player
        row (int): row of the board
        col (int): column of the board
        """
        # has correct bounds
        if (row >= 0) and (row <= 2) and (col >= 0) and (col <= 2):

            if self.board[row][col] == ' ':
                self.board[row][col] = turn
                return True                                       
            else:
                raise InvalidMoveError
        else:
            raise InvalidMoveError

    """     
    def update_game_board(self, row, col, move):
            if self.board[row][col] == ' ':
                self.board[row][col] = move
                self.last_player_turn = self.player_username
                return True  # Move successful
            else:
                return False  # Cell already occupied """

    def isWinner(self) -> bool:
        """
        Checks whether  the diagonals, rows, columns include all Xs or Os,
        if so, set the wins/losses (+1) and returns a bool to indicate that the game is finished.
        """

        for row in range(3):
            if self.board[row][0] == "X" and self.board[row][1] == "X" and self.board[row][2] == "X":
                if self.current_player == self.player_one:
                    self.num_wins += 1
                else:
                    self.num_losses += 1

                return True

        for col in range(3):
            if self.board[0][col] == "X" and self.board[1][col] == "X" and self.board[2][col] == "X":
                if self.current_player == self.player_one:
                    self.num_wins += 1
                else:
                    self.num_losses += 1
                return True

        if self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X":
            if self.current_player == self.player_one:
                self.num_wins += 1
            else:
                self.num_losses += 1

            return True

        if self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X":
            if self.current_player == self.player_one:
                self.num_wins += 1
            else:
                self.num_losses += 1

            return True

        for row in range(3):
            if self.board[row][0] == "O" and self.board[row][1] == "O" and self.board[row][2] == "O":
                if self.current_player == self.player_two:
                    self.num_wins += 1
                else:
                    self.num_losses += 1

                return True

        for col in range(3):
            if self.board[0][col] == "O" and self.board[1][col] == "O" and self.board[2][col] == "O":
                if self.current_player == self.player_two:
                    self.num_wins += 1
                else:
                    self.num_losses += 1

                return True

        if self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O":
            if self.current_player == self.player_two:
                self.num_wins += 1
            else:
                self.num_losses += 1

            return True

        if self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O":
            if self.current_player == self.player_two:
                self.num_wins += 1
            else:
                self.num_losses += 1

            return True

        return False

    def board_is_full(self):
        # Check if the board is full
        for row in self.board:
            for col in row:
                if col == ' ':
                    return False

        return True

    def print_stats(self):
        print('Player One: ', self.player_one)
        print('Player Two: ', self.player_two)
        print("Last player to move:", self.last_player_turn)
        print("Number of games played:", self.total_games_played)
        print("Number of wins:", self.num_wins)
        print("Number of losses:", self.num_losses)
        print("Number of ties:", self.num_ties)
