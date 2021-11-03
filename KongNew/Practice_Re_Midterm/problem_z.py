# Get the price for 1, 2, and 3 trucks
price_list = list(map(int, input().split()))
# print(price_list)

# Get the arrival and departure time
truck = [list(map(int, input().split())) for i in range(3)]
# print(truck)

total_price = 0
# For loop with range of maximum departure time
for i in range(max(truck[0][1], truck[1][1], truck[2][1])):
    cur = 0
    # Count how many truck are currently parking
    if i in range(truck[0][0], truck[0][1]):
        cur += 1
    if i in range(truck[1][0], truck[1][1]):
        cur += 1
    if i in range(truck[2][0], truck[2][1]):
        cur += 1
    # Add the price according to the price table
    total_price += cur * price_list[cur-1]
print(total_price)
