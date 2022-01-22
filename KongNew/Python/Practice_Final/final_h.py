n, t = map(int, input().split())

line = list(map(int, input().split()))
task = 0
for i in line:
    t -= i
    if t <= 0:
        break
    task += 1
print(task)
