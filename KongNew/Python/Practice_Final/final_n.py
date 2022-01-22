for i in range(int(input())):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))

    v1.sort(reverse=True)
    v2.sort()

    result = 0
    for j in range(n):
        result += v1[j] * v2[j]
    print("Case #" + str(i+1) + ": " + str(result))
