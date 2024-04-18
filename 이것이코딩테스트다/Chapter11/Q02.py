s = input()

sum = 0

for i in s:
    if sum <= 1 or int(i) <= 1:
        sum += int(i)
    else:
        sum *= int(i)
print(sum)