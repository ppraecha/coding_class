def sum_all(n):
    return int((n/2)*(n+1))


def sum_odd(n):
    return n*n


def sum_even(n):
    return n*(n+1)


for i in range(1, int(input())+1):
    user_input = list(map(int, input().split()))
    print(user_input[0], sum_all(user_input[1]), sum_odd(user_input[1]), sum_even(user_input[1]))
