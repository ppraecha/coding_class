x = []
y = []

for i in range(int(input())):
    user_input = input().split()
    x.append(int(user_input[0]))
    y.append(int(user_input[1]))

min_x = min(x)
max_x = max(x)
min_y = min(y)
max_y = max(y)

x_dis = max_x - min_x
y_dis = max_y - min_y

if x_dis > y_dis:
    print(x_dis**2)
else:
    print(y_dis**2)
