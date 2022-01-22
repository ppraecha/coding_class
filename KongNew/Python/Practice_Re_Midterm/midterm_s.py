def check_land(r, c):
    global seen
    # Check if already checked
    if (r, c) in seen:
        return
    # Check if out of range
    if r < 0 or r >= height:
        return
    if c < 0 or c >= width:
        return
    # Add to seen
    seen.add((r, c))
    # Ignore water
    if grid[r][c] == "W":
        return
    # Assume cloud next to land is same land
    if grid[r][c] == "C":
        grid[r][c] = "L"
    check_land(r - 1, c)
    check_land(r + 1, c)
    check_land(r, c - 1)
    check_land(r, c + 1)


# Take input
height, width = map(int, input().split())
grid = []
island = 0
seen = set()

# Get rows
for i in range(height):
    grid.append(list(input()))

# Check every row and col
for row in range(height):
    for col in range(width):
        if grid[row][col] == "L" and (row, col) not in seen:
            island += 1
            check_land(row, col)

print(island)
