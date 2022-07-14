from itertools import combinations

n, m = map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))

# 치킨집의 위치
chicken_loc = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 2:
            chicken_loc.append((i,j))

# 집들의 위치
house_loc = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            house_loc.append((i,j))

chicken_comb = list(combinations(chicken_loc,m))
answer_list = []
dist_list = []
distance_list = []

for co in chicken_comb: # 치킨집 좌표의 조합중에서 최단거리 찾기
    for i,j in house_loc:
        for x,y in co:  # 집별로 치킨거리 구하기
            dist_list.append(abs(i-x) + abs(j-y))
        distance_list.append(min(dist_list))
        dist_list = []
    answer_list.append(sum(distance_list))
    distance_list = []

print(min(answer_list))