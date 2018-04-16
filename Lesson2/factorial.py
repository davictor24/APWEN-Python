# Get input
# The int() function casts the input to an integer
n = int(input("Enter n: "))

# Initialize the accumulator variable
# The identity element for multiplication is 1
# Hence it is initialized to 1
fact = 1

# Loop and accumulate product
for i in range(1, n + 1):
    fact *= i

# Print answer
print(str(n) + "! = " + str(fact))
