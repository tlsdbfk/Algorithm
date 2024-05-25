data = input()

result = []
num = 0

for d in data:
    if d in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        num += int(d)
    else:  
        result.append(d)

result.sort()

answer = ""
for r in result:
    answer += r

print(answer + str(num))