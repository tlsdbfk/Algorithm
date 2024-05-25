n = int(input())

str_n = str(n)
len_n = len(str_n)

sum1 = 0

for i in range(len_n // 2):
    sum1 += int(str_n[i])

sum2 = 0
for i in range(len_n // 2, len_n):
    sum2 += int(str_n[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")