n = int(input())
if n % 2 != 0:
    print("still running")
    exit(0)

time = 0
for i in range(n//2):
    t1 = int(input())
    t2 = int(input())
    time += t2 - t1

print(time)
