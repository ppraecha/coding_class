import numpy as np

# Take input and store it as a 2D array
board = [list(input()) for i in range(int(input()))]
# print(board)

# Check the row
for row in board:
    # If the white and black tiles are not equal
    if row.count('W') != row.count('B'):
        print(0)
        exit(0)
    # If there are three consecutive tiles
    if 'WWW' in row or 'BBB' in row:
        print(0)
        exit(0)

# Check the column
transpose_board = np.transpose(board)
# print(transpose_board)
for col in board:
    # If the white and black tiles are not equal
    if col.count('W') != col.count('B'):
        print(0)
        exit(0)
    # If there are three consecutive tiles
    if 'WWW' in col or 'BBB' in col:
        print(0)
        exit(0)

print(1)
