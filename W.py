def print_w():
    for row in range(7):
        for col in range(7):
            if col == 0 or col == 6 or (col == row and row > 3) or (col + row == 6 and row > 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_w()
