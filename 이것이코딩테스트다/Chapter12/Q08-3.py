s = input()

sum = 0
text = []

for i in s:
    if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        sum += int(i)
    else:
        text.append(i)

text.sort()

result = ""

for t in text:
    result += t

print(result + str(sum))