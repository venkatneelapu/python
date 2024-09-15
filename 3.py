n = 5  # Size of the pattern

# Print the number 3 pattern using stars
for i in range(n):
    if i == 0 or i == n - 1 or i == n // 2:
        print('*' * n)
    else:
        print(' ' * (n // 2) + '*')
