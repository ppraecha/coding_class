w = int(input())
h = int(input())

for i in range(h):
    cur = i % 3
    for j in range(w):
        print(cur, end="")
        cur = (cur+1) % 3
    print()
