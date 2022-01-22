n = int(input())
num = list(filter(lambda i: i < 0, list(map(int, input().split()))))
print(sum(num)*-1)
