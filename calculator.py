"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# This is a program that runs until we press q
    # Initialize input string variable asks enter equation 
    # Initialize variable tokens as the tokenized version of input string
    # Develop conditionals for each function:
    # If input_string is 'q', break
    # If tokens at index 0 is '+'
    # Call the add function passing in the arguments, integers of tokens[1],[2]
    # Else if tokens at index 0 is '-'
    # Call the subtract function passing in the aguments same as for add function
    # Otherwise if tokens at index 0 is '*'
    # Call the multiply function passing in the same arguments as add function
    # Otherwise if tokens at index 0 is '/'
    # Call the divide function passing in the same arguments as in add
    # Otherwise if tokens at index 0 is 'square'
    # Call the square function, passing in only tokens at index 1
    # Otherwise if tokens at index 0 is 'cube'
    # Call the cube funcion, passing in only tokens at index 1
    # Otherwise if tokens at index 0 is 'pow'
    # Call the power function, passing in tokens at index 1 and 2
    # Otherwise if tokens at index 0 is 'mod', 
    # Call the mod function, passing in tokens at index 1 and 2
    # Otherwise print invalid equation, try again
while True:
    input_string = input("Enter equation:  ")
    tokens = input_string.split(' ')
    
    if input_string == 'q':
        break
    if tokens[0] == '+':
        print(add(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '-':
        print(subtract(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '*':
        print(multiply(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == '/':
        print(divide(float(tokens[1]), float(tokens[2])))
    elif tokens[0] == 'square':
        print(square(float(tokens[1])))  
    elif tokens[0] == 'cube':
        print(cube(float(tokens[1])))
    elif tokens[0] == 'pow':
        print(power(float(tokens[1]),float(tokens[2]))) 
    elif tokens[0] == 'mod':
        print(mod(float(tokens[1]), float(tokens[2])))
    else:
        print("Invalid input. Please enter a new equation.")
