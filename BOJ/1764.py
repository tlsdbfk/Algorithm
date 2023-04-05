n, m = map(int, input().split())

n_set = set()
m_set = set()

for i in range(n):  
    n_set.add(str(input()))

for i in range(m):  
    m_set.add(str(input()))

intersection = n_set.intersection(m_set)
intersection = sorted(intersection)

print(len(intersection))
for i in intersection:
    print(i)