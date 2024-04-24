from itertools import combinations

N, M = map(int, input().split())

board = []

for i in range(N):
    board.append(list(map(int, input().split())))

house_list = []
chicken_list = []

for x in range(N):
    for y in range(N):
        if board[x][y] == 1:
            house_list.append((x, y))
        elif board[x][y] == 2:
            chicken_list.append((x, y))

candidates = list(combinations(chicken_list, M))

def get_sum(candidates):
    result = 0
    for hx, hy in house_list:
        temp = 10000000000
        for cx, cy in candidates:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    
    return result

result = 10000000000

for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)

'''
distance_list = []

for chicken in chicken_list:
    chicken_x, chicken_y = chicken

    distance = 0

    for house in house_list:
        house_x, house_y = house

        distance += (abs(chicken_x-house_x)+abs(chicken_y-house_y))
    
    distance_list.append(distance)


sorted_distance_list = sorted(range(len(distance_list)), key=lambda i: distance_list[i])
distance_list = [distance_list[i] for i in sorted_distance_list]
chicken_list = [chicken_list[i] for i in sorted_distance_list]

chicken_list = chicken_list[:M]

distance_list2 = []
distance = 0

for house in house_list:
    house_x, house_y = house
    tmp_list = []

    for chicken in chicken_list:
        chicken_x, chicken_y = chicken
        distance = (abs(chicken_x-house_x)+abs(chicken_y-house_y))
        tmp_list.append(distance)
    
    distance_list2.append(min(tmp_list))

print(sum(distance_list2))
'''