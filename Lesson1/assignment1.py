# Get input
# The 'input' function waits for user input, pausing program execution
# The 'float' function converts the numerical string input to a float
# An error is thrown if a non-numerical input is entered
# If we use the 'int' function, our program will be limited to integers
# and an error will be thrown if we try to enter a float
# Hence we use 'float', for generic purposes
x = float(input("Enter first number: ")) # asks user for first number
y = float(input("Enter second number: ")) # asks user for second number

# Perform computations
# The concatenation operator is used to format the output
# Floats are converted into strings before they can be concatenated
# Note the use of quotes in surrounding string literals
print(str(x) + " + " + str(y) + " = " + str(x + y)) # addition
print(str(x) + " - " + str(y) + " = " + str(x - y)) # subtraction
print(str(x) + " * " + str(y) + " = " + str(x * y)) # multiplication
print(str(x) + " / " + str(y) + " = " + str(x / y)) # division
print(str(x) + " ** " + str(y) + " = " + str(x ** y)) #exponentiation
print(str(x) + " // " + str(y) + " = " + str(x // y)) # floor division
print(str(x) + " % " + str(y) + " = " + str(x % y)) # modulo

# just for fun :)
print("\nThe \n\tEnd")
