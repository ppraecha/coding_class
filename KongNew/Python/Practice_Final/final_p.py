n = int(input())
hand = list(map(int, input().split()))
hand.sort()
score = sum(hand)

for i in range(n-1):
    if hand[i] + 1 == hand[i+1]:
        score -= hand[i+1]

print(score)
