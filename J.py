# Function to print alphabet J
def print_J():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'J'
            if i == 0:  # Top horizontal line of 'J'
                print("*", end="")
            elif j == cols // 2 and i != rows - 1:  # Vertical line of 'J'
                print("*", end="")
            elif i == rows - 1 and j < cols // 2:  # Bottom horizontal hook of 'J'
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'J'
print_J()
