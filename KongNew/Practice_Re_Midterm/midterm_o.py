stars = int(input())
print(str(stars)+":")

for i in range(2, stars//2 + 1):
    # i and i - 1 end with i
    if stars % (i + i - 1) == i:
        print(i, i - 1)
    # i and i - 1 end with i - 1
    if stars % (i + i - 1) == 0:
        print(i, i - 1)
    # i and i
    if stars % i == 0:
        print(i, i)
