days = set()

for i in range(int(input())):
    date = list(map(int, input().split()))
    for day in range(date[0], date[1]+1):
        days.add(day)

print(len(days))
