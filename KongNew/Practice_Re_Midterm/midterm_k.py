n = int(input())
seq = list(map(int, input().split()))
tower = 1

for i in range(1, n):
    if seq[i] > seq[i-1]:
        tower += 1

print(tower)
