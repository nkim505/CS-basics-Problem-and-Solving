# 실패: 결과 - 출력초과

n = int(input())
k = int(input())

graph = [[0]*n for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 999

l = int(input())
direction_list = []
turn_list = []
for i in range(l):
    x, c = input().split()
    turn_list.append(int(x))
    direction_list.append(c)

turn_dict = dict(zip(turn_list, direction_list))



cur_loc = [0,0]
cnt = 0

# 일반, D, L 순서
dx = [0, 1, -1] 
dy = [1, 0, 0 ]

queue = deque()
queue.append(cur_loc)

while 1:
    
    cnt += 1
    
    
    # 뱀 머리 좌표 옮기기
    if cnt not in turn_list:
        cur_loc[0] += dx[0]
        cur_loc[1] += dy[0]
        
    elif cnt in turn_list:
        if turn_dict[cnt] == 'D':
            cur_loc[0] += dx[1]
            cur_loc[1] += dy[1]
        elif turn_dict[cnt] == 'L':
            cur_loc[0] += dx[2]
            cur_loc[1] += dy[2]
    
    queue.append(cur_loc)
    print(queue)
    
    # 사과의 유무에 따라 뱀 꼬리 위치가 줄어들지 아닐지
    if graph[cur_loc[0]][cur_loc[1]] != 999: #사과가 없는 자리라면
        queue.popleft()
    
    print(queue)
    # 머리가 꼬리와 닿는지 아닌지, 벽에 닿는지 확인
    if cur_loc[1]> n-1 or cur_loc[0] < 0 or cur_loc[0] > n-1:
        break
    
    elif (len(queue) > 2) and (cur_loc == queue[0]):
        break

print(cnt)
    
        
    
    
