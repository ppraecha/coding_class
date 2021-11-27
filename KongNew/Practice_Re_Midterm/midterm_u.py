# Take the row input
lines = []
for i in range(int(input())):
    # Get the line of input and convert to int
    line = list(map(int, input().split()))
    # Put the gnomes into the line except the first element, which is the number of gnomes
    lines.append(line[1:len(line)])

# print(lines)
# Check through the lines of gnomes
for line in lines:
    # Loop through every item except first and last
    for i in range(1, len(line)):
        # If reach the second to the last gnomes, that gnomes is the king
        if i == len(line)-1:
            print(line.index(line[i-1])+1)
            break
        # Check if a gnomes is out of order
        if line[i] < line[i-1]:
            if line[i-1] > line[i+1]:
                print(line.index(line[i-1])+1)
            else:
                print(line.index(line[i])+1)
            break
