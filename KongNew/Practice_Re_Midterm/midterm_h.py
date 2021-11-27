import numpy as np

word_array = []
for i in range(int(input())):
    # Take user input
    word = input()

    # Create a 4x4 table
    word_table = []
    for j in range(0, 4):
        word_table.append(word[j*4:(j+1)*4])

    # Change empty element to *
    for r in range(len(word_table)):
        if len(word_table[r]) != 4:
            temp = "*" * (4-len(word_table[r]))
            word_table[r] = word_table[r] + temp

    # Transpose the word table
    word_table = list(map(list, word_table))
    word_table = word_table[::-1]
    word_table = np.transpose(word_table)

    # Print the word but skip *
    for row in word_table:
        for col in row:
            if col != "*":
                print(col, end="")
    print()
