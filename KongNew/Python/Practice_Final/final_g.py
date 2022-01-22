import numpy as np
import math as m

for i in range(int(input())):
    word = input()

    square = int(m.sqrt(len(word)))
    word_table = []
    for j in range(0, square):
        word_table.append(list(word[j*square:(j+1)*square]))

    word_table = word_table[::-1]
    word_table = np.transpose(word_table)

    result = []
    for row in word_table:
        result.extend(row)

    result = result[::-1]
    print("".join(result))