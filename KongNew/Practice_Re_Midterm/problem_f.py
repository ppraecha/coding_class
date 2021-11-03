# Get the input and create the board of knight as a list of strings
board = [input() for i in range(5)]
# print(board)

# There should be a total of 9 knights on the board
knight_cnt = 0
# Create a flag for validity
valid = True
# Go through every position on the board
for i in range(5):
    # Stop the loop if the result is already invalid
    if not valid:
        break
    for j in range(5):
        # If the position is a knight, perform check and track the number
        if board[i][j] == 'k':
            knight_cnt += 1
            # Avoid out of range while check all the possible move position
            if i > 0 and j > 1:
                if board[i-1][j-2] == 'k':
                    valid = False
            if i > 1 and j > 0:
                if board[i-2][j-1] == 'k':
                    valid = False
            if i > 0 and j < 3:
                if board[i-1][j+2] == 'k':
                    valid = False
            if i > 1 and j < 4:
                if board[i-2][j+1] == 'k':
                    valid = False
            if i < 4 and j > 1:
                if board[i+1][j-2] == 'k':
                    valid = False
            if i < 3 and j > 0:
                if board[i+2][j-1] == 'k':
                    valid = False
            if i < 4 and j < 3:
                if board[i+1][j+2] == 'k':
                    valid = False
            if i < 3 and j < 4:
                if board[i+2][j+1] == 'k':
                    valid = False

# print(knight_cnt)
# Check the number of knight first
if knight_cnt != 9:
    print("invalid")
# Check the validity of the puzzle
elif valid:
    print("valid")
else:
    print("invalid")
