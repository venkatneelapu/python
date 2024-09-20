# Number of rows and columns
rows = 7

for i in range(1, rows + 1):
    if i == 1 or i == rows // 2 + 1 or i == rows:
        print('*' * (rows - 1))  # Top, middle, and bottom horizontal lines
    elif i < rows // 2 + 1:
        print('*' + ' ' * (rows - 2) + '*')  # Top half vertical lines
    else:
        print(' ' * (rows - 1) + '*')  # Bottom half vertical line on the right
