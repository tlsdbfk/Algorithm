n = str(input())

left = 0

for i in range(len(n) // 2):
    left += int(n[i])

right = 0

for i in range(len(n) // 2, len(n)):
    right += int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")