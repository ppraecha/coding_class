for case in range(int(input())):
    size = list(map(int, input().split()))
    grid = []
    for row in range(size[0]):
        grid.append(list(input())[::-1])
    grid = grid[::-1]
    print("Test", case+1)
    for row in grid:
        print("".join(row))
