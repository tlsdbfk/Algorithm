input_data = input()

num_list = []
str_list = []

for i in input_data:
    if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        num_list.append(i)
    else:
        str_list.append(i)
    
str_list.sort()

answer = ""

for s in str_list:
    answer += s

sum = 0

for n in num_list:
    sum += int(n)

print(answer + str(sum))