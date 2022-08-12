
import sys
input = sys.stdin.readline

n = int(input())
eggs = [] # 0번째 채우기
for _ in range(n):
    tmp = list(map(int,input().split()))
    eggs.append(tmp)
    
result = 0
duration, weight = 0, 1

def dfs(curr_idx):
    global result
    
    #종료조건
    if curr_idx == n: #가장 마지막까지 지나오면
        cnt = 0 #깨진달걀 수 초기화
        for i in range(n):
            if eggs[i][duration] <= 0 : # 깨지면
                cnt += 1 #깨진 달걀 몇개인지 cnt
        result = max(result, cnt)
        return
    
    #다음 계란으로 넘어가기
    if eggs[curr_idx][duration] <= 0 : #지금 손에 든 달걀이 깨진거면
        dfs(curr_idx + 1)
        return
    
    #손에 든 것 제외, 모두 깨져있을 경우
    isAllBroken = True
    
    for i in range(n):
        if i == curr_idx:
            continue
        if eggs[i][duration] > 0: # 하나라도 안깨진게 있으면
            isAllBroken = False
            break
            
    if isAllBroken:
        result = max(result, n-1) #최근까지의 result 업뎃값과 n-1에서 max 선택
        return

    
    #계란치기 수행
    for i in range(n):
        if i == curr_idx:
            continue
        if eggs[i][duration] <= 0:
            continue
        
        #때리기
        eggs[curr_idx][duration] -= eggs[i][weight]
        eggs[i][duration] -= eggs[curr_idx][weight]
        dfs(curr_idx + 1) #깊이탐색 시작
        
        #깊이 탐색 마두리 후 다시 duration 상태 복구
        eggs[curr_idx][duration] += eggs[i][weight]
        eggs[i][duration] += eggs[curr_idx][weight]
        
dfs(0)
print(result)

# 
