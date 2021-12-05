w, p = map(int, input().split())
portion = list(map(int, input().split()))
possible_space = {w}

for i in portion:
    possible_space.add(i)
    possible_space.add(w-i)
    for j in portion:
        if i == j:
            break
        possible_space.add(i-j)

sorted_space = sorted(list(possible_space))
print(*sorted_space)
