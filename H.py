# Function to print alphabet H
def print_H():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'H'
            if j == 0 or j == cols - 1:  # Left and right vertical lines of 'H'
                print("*", end="")
            elif i == rows // 2:  # Middle horizontal line of 'H'
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'H'
print_H()
