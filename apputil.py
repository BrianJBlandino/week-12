import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt

def update_board(current_board):
    """Creating a function that takes in a binary NumPy array,
    and executes one step of Conway's game of life for this array."""
    
    # Create a copy to store the next state
    new_board = np.zeros(board.shape, dtype=int)
    
    # Define neighbors' relative positions
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1),          (0, 1),
                 (1, -1),  (1, 0),  (1, 1)]
    
    # Iterate over each cell
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            # Count live neighbors
            live_neighbors = sum(
                board[(i + dx) % board.shape[0], (j + dy) % board.shape[1]]
                for dx, dy in neighbors
            )
                # Apply Conway's rules
            if board[i, j] == 1:
                # Currently alive
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[i, j] = 0  
                else:
                    new_board[i, j] = 1  
            else:
                # Currently dead
                if live_neighbors == 3:
                    new_board[i, j] = 1  
                    
    updated_board = current_board
    
    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='plasma', cbar=False, square=True)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)