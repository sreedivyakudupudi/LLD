class Board:
    def __init__(self, size=3):
        self.size = size
        self.grid = [
            [" " for _ in range(size)]
            for _ in range(size)
        ]

    def display(self):
        print()

        for row in range(self.size):
            print(" " + " | ".join(self.grid[row]))

            if row < self.size - 1:
                print("---+" + "---+" + "---")

        print()

    def is_valid(self, row, col):
        return (
            0 <= row < self.size
            and 0 <= col < self.size
        )

    def is_empty(self, row, col):
        return self.grid[row][col] == " "

    def place_symbol(self, row, col, symbol):
        if not self.is_valid(row, col):
            return False

        if not self.is_empty(row, col):
            return False

        self.grid[row][col] = symbol
        return True

    def check_winner(self, row, col, symbol):

        # Check the row containing the latest move
        if all(
            self.grid[row][c] == symbol
            for c in range(self.size)
        ):
            return True

        # Check the column containing the latest move
        if all(
            self.grid[r][col] == symbol
            for r in range(self.size)
        ):
            return True

        # Check the main diagonal
        if row == col:
            if all(
                self.grid[i][i] == symbol
                for i in range(self.size)
            ):
                return True

        # Check the anti-diagonal
        if row + col == self.size - 1:
            if all(
                self.grid[i][self.size - 1 - i] == symbol
                for i in range(self.size)
            ):
                return True

        return False

    def is_full(self):
        return all(
            self.grid[row][col] != " "
            for row in range(self.size)
            for col in range(self.size)
        )
