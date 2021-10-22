word = input().upper()

# Init variable
result = ""
temp_cnt = 0
cur = word[0]

# Go through the word
for letter in word:
    # Change the letter
    if letter != cur:
        # Save the current count with the letter
        if temp_cnt != 1:
            result += str(temp_cnt) + cur
        else:
            result += cur
        # Change current letter to the new letter
        cur = letter
        # Reset the temp_cnt
        temp_cnt = 0

    # Count the current letter
    temp_cnt += 1

# Save the current count with the letter
if temp_cnt != 1:
    result += str(temp_cnt) + cur
else:
    result += cur

print(result)