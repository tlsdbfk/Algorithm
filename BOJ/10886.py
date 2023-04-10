n = int(input())

notcute = 0
cute = 0

for i in range(n): 
    a = int(input())
    if a == 0:
        notcute += 1
    else:
        cute += 1

if cute > notcute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
