word_ls = []
n = int(input())
for i in range(n*2):
    word_ls.append(input())

for i in range(0, len(word_ls), 2):
    word1 = word_ls[i]
    word2 = word_ls[i+1]

    print(word1)
    print(word2)
    for j in range(len(word1)):
        if word1[j] == word2[j]:
            print(".", end="")
        else:
            print("*", end="")
    print("\n")
