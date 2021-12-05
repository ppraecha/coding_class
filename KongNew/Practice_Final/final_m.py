n, p = map(int, input().split())
listener = list(map(int, input().split()))
price = sum(listener) - n*p

for i in range(1, n):
    cur = listener[0:n-i]
    # print(cur)
    if price <= sum(cur) - (len(cur))*p:
        price = sum(cur) - (len(cur))*p
        listener = cur

for i in range(1, len(listener)):
    cur = listener[i:len(listener)]
    # print(cur)
    if price <= sum(cur) - (len(cur)) * p:
        price = sum(cur) - (len(cur)) * p

print(price)
