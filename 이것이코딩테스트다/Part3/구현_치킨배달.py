from numpy import append

def calculate_dist(loc1, loc2):
    result = abs(loc1[1] - loc2[1]) + abs(loc1[2] - loc2[2])
    return result

N, M = map(int, input("input numbers: ").split())

graph = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)





all_dist = []
dist = []






print(sum(all_dist))
