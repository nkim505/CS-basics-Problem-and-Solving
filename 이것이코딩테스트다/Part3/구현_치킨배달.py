from numpy import append

def calculate_dist(loc1, loc2):
    result = abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])
    return result

def make_houselist(graph, n):
    house_list = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                house_list.append((i,j))
    return house_list


N, M = map(int, input("input numbers: ").split())

graph = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

house_list = make_houselist(graph, N)
all_dist = []

for house in house_list:
    dist = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2: #해당 위치가 치킨집이면 치킨거리 계산
                tmp = calculate_dist(house,(i,j))
                dist.append(tmp)

    all_dist.append(min(dist))

print(sum(all_dist))
