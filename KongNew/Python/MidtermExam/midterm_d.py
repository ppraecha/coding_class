# Take input
word = input()
# Initial Value
word_set = set()
double_set = set()

# Split word into every combination
for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        word_set.add(word[i:j])

# Check for the longest double string
for i in word_set:
    # Odd length
    if len(i) % 2 != 0:
        continue
    # Split into left and right
    left = i[0:len(i)//2]
    right = i[len(i)//2:len(i)]
    # Check if left and right is equal and add to set
    if left == right:
        double_set.add(i)

longest = None
for i in double_set:
    # First item
    if longest is None:
        longest = i
    elif len(longest) < len(i):
        longest = i

print(longest)
