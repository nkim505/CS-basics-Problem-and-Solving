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
all_dist = sorted(all_dist, key = lambda x : x[0])

all_dist = all_dist[0:M]


# to be continue..

print(all_dist)
'''
