n = int(input())
while n != 0:
    time = []
    am = []
    pm = []
    am12 = []
    pm12 = []
    for i in range(n):
        t = input().split()
        temp = list(map(int, t[0].split(":")))
        if t[1] == "a.m.":
            if temp[0] == 12:
                am12.append(temp)
            else:
                am.append(temp)
        else:
            if temp[0] == 12:
                pm12.append(temp)
            else:
                pm.append(temp)
    am.sort()
    am12.sort()
    pm.sort()
    pm12.sort()
    for i in am12:
        print(i[0], ":", f'{i[1]:02}', " a.m.", sep="")
    for i in am:
        print(i[0], ":", f'{i[1]:02}', " a.m.", sep="")
    for i in pm12:
        print(i[0], ":", f'{i[1]:02}', " p.m.", sep="")
    for i in pm:
        print(i[0], ":", f'{i[1]:02}', " p.m.", sep="")
    # print(am12, am, pm12, pm, sep="\n")
    print()
    n = int(input())
