n, k = map(int, input().split())
rating = 0
for i in range(k):
    rating += int(input())

min_rate = round((rating+((n-k)*-3))/n, 4)
max_rate = round((rating+((n-k)*3))/n, 4)
print(min_rate, max_rate)
