line = list(input().split(";"))
for i in range(len(line)):
    if "-" in line[i]:
        s, f = list(map(int, line[i].split("-")))
        line[i] = f - s + 1
    else:
        line[i] = 1

print(sum(line))
