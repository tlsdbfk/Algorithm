input_data = input()

text_list = []
num_list = []

for i in input_data:
    if i in ["1","2","3","4","5","6","7","8","9","0"]:
        num_list.append(int(i))
    else:
        text_list.append(i)

text_list = sorted(text_list)

answer = ""

for t in text_list:
    answer += t

answer += str(sum(num_list))

print(answer)