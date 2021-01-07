"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

# Loop until told to break
    # Create variable, input_string that asks the user to input, "Enter an equation > "
    # Split string_input into a list at ' ' delimiter
    # If input_string is 'q'
    # Break from the loop
    # Otherwise,
    # If tokens at index 0 is '+'
    # Call the add function passing in two arguments, floats of tokens[1], [2]
    # Else if tokens at index 0 is '-'
    # Call the subtract function passing in two arguments, floats of tokens[1], [2]
    # Otherwise if tokens at index 0 is '*'
    # Call the multiply function passing in two arguments, floats of tokens[1], [2]
    # Otherwise if tokens at index 0 is '/'
    # Call the divide function passing in two arguments, floats of tokens[1], [2]
    # Otherwise if tokens at index 0 is 'square'
    # Call the square function passing in one argument, float of tokens[1]
    # Otherwise if tokens at index 0 is 'cube'
    # Call the cube function passing in one argument, float of tokens[1]
    # Otherwise if tokens at index 0 is 'pow'
    # Call the power function passing in two arguments, floats of tokens[1], [2]
    # Otherwise if tokens at index 0 is 'mod', 
    # Call the mod function passing in two arguments, floats of tokens[1], [2]
    # Otherwise print invalid equation, try again
while True:
    input_string = input("Enter an equation > ")
    tokens = input_string.split(' ')
    
    if input_string == 'q':
        break
    else:
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
