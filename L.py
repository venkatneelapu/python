# Function to print alphabet L
def print_L():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'L'
            if j == 0:  # Left vertical line of 'L'
                print("*", end="")
            elif i == rows - 1:  # Bottom horizontal line of 'L'
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'L'
print_L()
