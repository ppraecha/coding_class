word = input()
guess = input()
strike = 0
correct = 0
n = len(word)

for i in guess:
    if strike == 10:
        print("LOSE")
        break
    if correct == n:
        print("WIN")
        break
    if i in word:
        correct += word.count(i)
    else:
        strike += 1
