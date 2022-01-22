cipher = input()
key = input()
message = ""

for i in range(len(cipher)):
    shift = ord(key[i]) - 65
    after = ord(cipher[i]) - shift
    if after < 65:
        after += 26
    message += chr(after)
    key += message[i]

print(message)
