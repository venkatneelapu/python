# Function to print alphabet A
def print_A():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'A'
            if (j == 0 or j == cols - 1) and i != 0:  # Sides of the 'A'
                print("*", end="")
            elif i == 0 and (j != 0 and j != cols - 1):  # Top of the 'A'
                print("*", end="")
            elif i == rows // 2:  # Middle horizontal line of the 'A'
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'A'
print_A()
