# Number of rows
rows = 7

for i in range(1, rows + 1):
    if i == 1:
        print('*' * rows)  # Top horizontal line
    else:
        print(' ' * (rows - 1) + '*')  # Vertical line on the right side
