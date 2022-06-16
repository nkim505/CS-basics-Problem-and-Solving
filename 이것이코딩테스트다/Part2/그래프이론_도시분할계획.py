# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
        


# 노드 개수와 간선 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모테이블 초기화

#모든 간선을 담을 리스트와 각각의 유지비를 담을 리스트, 유지비 합 변수
edges = []
costs = []
result = 0

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해서 튜플 첫 번째 원소로 비용을 넣기
    edges.append((cost, a, b))

edges.sort() #간선을 비용 순으로 정렬 
    
# 비용이 가장 짧은 간선을 선택해서 집합에 포함 -> 반복하여, 비용이 작은 간선 선택해서 같은 집합에 들어 있지 않으면 union으로 포함
# 이미 동일한 집합에 포함되어 있으면 신장트리에 포함하지 않는다. -> union 호출하지 않음

# 크루스칼 알고리즘
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) !=find_parent(parent, b): #서로 동일한 집합이 아님
        union_parent(parent, a, b) # 집합에 포함
        costs.append(cost) #간선의 비용 저장
        result += cost

# 최종적으로 신장트리의 가장 비용이 큰 간선을 제외하고 합하기

result = result - max(costs)

print(result)
