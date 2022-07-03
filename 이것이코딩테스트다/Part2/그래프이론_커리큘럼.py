from collections import deque
import copy


#3
#30 -1
#20 -1
#40 1 2 -1

n = int(input())

# 모든 노드에 대한 진입차수는 0으로 초기화 
indegree = [0]*(n+1)
#[0, 0, 0, 0]

# 각 노드에 연결된 정보를 담기 위한... 
graph = [[] for i in range(n+1)]
#[[] [] [] []]

# 각 노드까지의 시간 
time = [0]*(n+1)
#[0, 0, 0, 0]

# 방향 그래프의 모든 간선 정보를 입력 받기
for i in range(1, n+1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for x in info[1:-1]:
        indegree[i] += 1
        graph[x].append(i) #선수강 과목 idx에 후수강 과목번호가 element로 들어감 

#time == [0, 30, 20 , 40]
#indegree == [0, 0, 0, 0]
#graph == [[] [3] [3] []]

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 각 강의의 최대 시간을 담을 리스
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0: # [0, 0, 0, 2]
            q.append(i)
  
    # 큐가 빌 때까지 반복

    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft() #3
         
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]: #graph == [[] [3] [3] []]
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
		# result == [0, 30, 20 , 70]
    for i in range(1, n+1):
        print(result[i])
        
topology_sort()
