def print_y():
    size = 7
    for row in range(size):
        for col in range(size):
            if (col == row and row < size // 2) or (col + row == size - 1 and row < size // 2) or (col == size // 2 and row >= size // 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_y()
