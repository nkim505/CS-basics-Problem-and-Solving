from itertools import combinations #조합과 순열에서 itertools

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


'''
# 잘못 푼 코드
def calculate_dist(loc1, loc2):
    result = abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    return result

def make_chickenlist(graph, n):
    chicken_list = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                chicken_list.append((i,j))
    return chicken_list


N, M = map(int, input().split())

graph = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

chicken_list = make_chickenlist(graph, N)
all_dist = []

for chicken in chicken_list:
    dist = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1: #해당 위치가 일반집이면 치킨거리 계산
                tmp = calculate_dist(chicken,(i,j))
                dist.append(tmp)

    all_dist.append((min(dist), chicken))

print(all_dist)

'''
