def print_v():
    for row in range(7):
        for col in range(7):
            if (col == row and row < 4) or (col + row == 6 and row < 4):
                print("*", end="")
            elif row >= 4 and (col == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_v()
