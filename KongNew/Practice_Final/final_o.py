ls = []
for i in range(int(input())):
    ls.append(str(i))

for i in range(len(ls)):
    cur = ls[i]
    if cur[0] == "0":
        print(1)
