n = input()

n_list = []

for i in n:
    n_list.append(int(i))

if sum(n_list[:len(n)//2]) == sum(n_list[len(n)//2:]):
    print("LUCKY")
else:
    print("READY")