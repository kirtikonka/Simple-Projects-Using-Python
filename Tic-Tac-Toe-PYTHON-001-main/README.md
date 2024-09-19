# Tic-Tac-Toe

**Functions:**

 `sum(a, b, c)`: This is a simple function that takes three numbers (a, b, and c) and returns their sum. It's used later to check if a player has three marks in a winning position.

 `printBoard(xState, yState)`: This function takes two lists, `xState` and `yState`, representing the game board state for player X and player O respectively. It iterates through these lists and displays the board in a formatted way using f-strings. Positions on the board are represented by numbers (0-8) which are replaced with "X" for player X marks, "O" for player O marks, or the position number itself if empty. 

 `checkWin(xState, yState)`: This function is responsible for checking if there's a winner. It has a list `wins` that defines all the possible winning combinations (rows, columns, and diagonals) as lists of indexes. The function iterates through each winning combination in `wins`. For each combination (represented by a list of indexes `[win[0], win[1], win[2]]`), it calls the `sum` function on the corresponding elements in `xState` and `yState` to see if the sum equals 3 (indicating three X's) or 0 (indicating three O's). If a sum matches either condition, it prints the winner ("X won the match" or "O won the match") and returns 1 (signaling a win). Otherwise, it returns -1 (indicating no winner yet).

**Main Program:**

 The `if __name__ == "__main__":` block ensures the following code only runs when the script is executed directly, not when imported as a module.

 Inside the block, two lists `xState` and `yState` are initialized with nine zeros, representing the empty board state for players X and O respectively.

 A variable `turn` is set to 1, which is used to track whose turn it is (1 for X, 0 for O).

 The program starts with a welcome message.

 A `while` loop keeps the game running until a winner is declared.

    * Inside the loop, the `printBoard` function is called to display the current board state.

    * Depending on the `turn` value, it prints either "X's Turn" or "O's Turn".

    * The player is prompted to enter a value representing their desired position on the board (0-8).

    * Based on the turn, the entered value is assigned as 1 (for X) or 0 (for O) in the corresponding player's state list (`xState` or `yState`).

    * The `checkWin` function is called to check if the recent move resulted in a win.

    * If `checkWin` returns 1 (indicating a win), the game is declared over, and the loop breaks.

    * Finally, the `turn` is switched to the other player (1 becomes 0 or 0 becomes 1) for the next turn.

**Limitations:**

This code does not currently handle ties (where all positions are filled without a winner). Additionally, there's no functionality to check for invalid moves (trying to place a mark on an already occupied position). 
