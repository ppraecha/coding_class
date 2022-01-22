n = input()
count = dict()

while n != "***":
    if n not in count:
        count[n] = 1
    else:
        count[n] += 1
    n = input()

count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
print(count)
name = list(count)
print(name)

if count[name[0]] == count[name[1]]:
    print("Runoff!")
else:
    print(name[0])
