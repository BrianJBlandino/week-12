import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt

def update_board(current_board):
    """Creating a function that takes in a binary NumPy array,
    and executes one step of Conway's Game of Life for this array."""
    
    # Create a copy to store the next state
    new_board = np.zeros(current_board.shape, dtype=int)
    
    # Get the number of rows and columns
    rows, cols = current_board.shape
    
    # Iterate over each cell
    for i in range(rows):
        for j in range(cols):
            
            # Count live neighbors without wrapping around edges
            live_neighbors = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue  
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < rows and 0 <= nj < cols:
                        live_neighbors += current_board[ni, nj]
            
            # Apply Conway's four rules
            if current_board[i, j] == 1:
                
                # Rule 1 & 3: Survive with 2 or 3 neighbors; otherwise die
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[i, j] = 0
                else:
                    new_board[i, j] = 1
            else:
                # Rule 4: Become alive if exactly 3 neighbors
                if live_neighbors == 3:
                    new_board[i, j] = 1
    
    # Setting the updated_board variable (to satisfy template)
    updated_board = new_board
    
    # Returning result
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