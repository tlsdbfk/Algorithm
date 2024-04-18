n = str(input())

index = len(n) // 2

left = n[:index]
right = n[index:]

left_sum = 0

for l in left:
    left_sum += int(l)

right_sum = 0

for r in right:
    right_sum += int(r)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")