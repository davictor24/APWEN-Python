# Get inputs a, b and c
# The coefficients, in general, can be floating-point numbers
# Hence cast to floats using the float() function
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Compute discriminant
D = b*b - 4*a*c

if D >= 0: # There are real roots
    # x1 and x2 could be equal
    # In that case, we would have real repeated roots
    # This happens when the discriminant, D = 0
    # Otherwise, there are real and distinct roots
    x1 = (-b + D**0.5) / (2*a) # first solution
    x2 = (-b - D**0.5) / (2*a) # second solution

    # Print solutions
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
    
else: # Complex conjugate roots
    # Get the real and imaginary parts
    # In finding the imaginary part, we find the square root of -D
    # This is because D itself is a negative number already
    re = -b / (2*a) # real part
    im = ((-D)**0.5) / (2*a) # imaginary part

    # Print solutions
    # x1 = re + j(im)
    # x2 = re - j(im)
    print("x1 = " + str(re) + " + j" + str(im))
    print("x2 = " + str(re) + " - j" + str(im))
