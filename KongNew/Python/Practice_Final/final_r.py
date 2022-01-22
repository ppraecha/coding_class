n = int(input())
na, nb, nc = 0, 0, 0
ya, yb, yc = 0, 0, 0

for i in range(n):
    case = input()
    if case[0] == "Y":
        if case[1] == "Y":
            ya += 1
        if case[2] == "Y":
            yb += 1
        if case[3] == "Y":
            yc += 1
    else:
        if case[1] == "Y":
            na += 1
        if case[2] == "Y":
            nb += 1
        if case[3] == "Y":
            nc += 1

result = (1 - ya/na, 1 - yb/nb, 1 - yc/nc)

for i in result:
    i = round(i, 8)
    if i <= 0:
        print("Not Effective")
    else:
        print(i*100)
