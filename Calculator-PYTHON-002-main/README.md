# Calculator-PYTHON-002

The code is for a basic calculator application built with Python and the Tkinter GUI library.

It defines a Calculator class that will handle all the calculator logic and UI elements.
In the init method, it creates the main window, display frames, and initializes variables to track the total and current expressions.
It has methods to create all the buttons like digits, operators, clear, equals etc and grid them out in the buttons frame.
The digit and operator buttons are bound to methods like add_to_expression and append_operator that update the expressions.
There are methods to evaluate the expression when equals is pressed, calculate square/square root, and update the display labels.
It also binds the keyboard keys to trigger the same methods as clicking the buttons.
The run method starts the Tkinter main loop to display the window.
