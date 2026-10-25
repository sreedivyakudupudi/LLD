
from Board import Board
from Player import Player

from Game import Game
def main():
    # Create the players
    player1 = Player(1, "Alice", "X")
    player2 = Player(2, "Bob", "O")

    # Create the board
    board = Board(size=3)

    # Create the game
    game = Game(board, [player1, player2])

    # Start the game
    game.start()


if __name__ == "__main__":
    main()