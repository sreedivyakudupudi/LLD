class Game:
    def __init__(self, board, players):
        if len(players) != 2:
            raise ValueError("Tic-Tac-Toe requires exactly two players.")

        if players[0].symbol == players[1].symbol:
            raise ValueError("Players must have different symbols.")

        if board.size < 1:
            raise ValueError("Board size must be positive.")

        self.board = board
        self.players = players
        self.current_player_index = 0
        self.winner = None
        self.game_over = False

    def switch_player(self):
        self.current_player_index = (
            1 - self.current_player_index
        )

    def make_move(self, row, col):
        if self.game_over:
            print("The game is already over.")
            return False

        if not self.board.is_valid(row, col):
            print("Invalid position. Choose a row and column from 1 to 3.")
            return False

        if not self.board.is_empty(row, col):
            print("Cell already occupied. Try another position.")
            return False

        player = self.players[self.current_player_index]

        self.board.place_symbol(
            row, col, player.symbol
        )

        # Check whether the current player has won
        if self.board.check_winner(
            row, col, player.symbol
        ):
            self.winner = player
            self.game_over = True
            self.board.display()

            print(f"{player.player_name} wins!")
            return True

        # Check for a draw after checking for a winner
        if self.board.is_full():
            self.game_over = True
            self.board.display()

            print("The game is a draw!")
            return True

        # Continue with the next player's turn
        self.switch_player()
        return True

    def start(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Enter row and column numbers from 1 to 3.")
        print("Player 1: X | Player 2: O")

        while not self.game_over:
            self.board.display()

            player = self.players[self.current_player_index]

            print(
                f"{player.player_name}'s turn "
                f"({player.symbol})"
            )

            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1

            except ValueError:
                print("Invalid input. Please enter integer coordinates.")
                continue

            self.make_move(row, col)
