**Global Variable:**

* `calculation`: This string variable stores the current user input for the calculation.

**Functions:**

* `add_to_calculation(symbol)`:
  * Takes a number or symbol as input.
  * Appends the symbol to the `calculation` string.
  * Clears the text result widget and inserts the updated `calculation`.
* `evaluate_calculation()`:
  * Tries to evaluate the `calculation` string as a mathematical expression using `eval`.
  * If successful, it updates the text result with the calculated value.
  * In case of errors (e.g., division by zero), it calls the `clear_field` function to clear and displays "Error" in the text result.
* `clear_field()`:
  * Clears the `calculation` string and the text result widget.

**GUI Layout:**

* The code creates a Tkinter main window (`root`).
* A text widget (`text_result`) is used to display the calculation and result.
* Multiple buttons are created for numbers (0-9), operators (+, -, *, /), parentheses (), and clear (C) and equals (=) functionalities.
* Each button is linked to a corresponding function using lambda functions for cleaner code.
  * Number buttons call `add_to_calculation` with the number as an argument.
  * Operator buttons call `add_to_calculation` with the operator symbol.
  * Parenthesis buttons call `add_to_calculation` with the parenthesis symbol.
  * Clear button calls `clear_field` to clear the input.
  * Equals button calls `evaluate_calculation` to evaluate the expression.
* The buttons are positioned in a grid layout using the `grid` method.

**Main Loop:**

* `root.mainloop()`: This starts the main event loop of the Tkinter application, listening for user interactions with the buttons and updating the display accordingly.
