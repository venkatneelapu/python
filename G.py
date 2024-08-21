# Function to print alphabet G
def print_G():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'G'
            if (j == 0 and (i != 0 and i != rows - 1)) or \
               (j == cols - 1 and i >= rows // 2) or \
               ((i == 0 or i == rows - 1 or i == rows // 2) and j != 0):  # Left, right, top, middle, and bottom lines
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'G'
print_G()
