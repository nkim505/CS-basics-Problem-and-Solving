def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 합치기 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
# 합치기 연산 수행
for i in range(e):
    func, a, b = map(int, input().split())
    if func == 0:
        union_parent(parent, a, b)
    else:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a==b:
            print('Yes')
        else:
            print('No')

