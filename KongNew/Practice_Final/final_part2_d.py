total = int(input())
h = int(input())

if total <= 0 or h <= 0:
    print("Invalid input")

for i in range(h):
    for j in range(total//h+1):
        cur = i+(j*h)+1
        if cur > total:
            break
        print(cur, end=" ")
    if i >= total:
        break
    print()
