def retate_90(m):
    N = len(m)
    ret = [[0]*N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def return_keyarray(key):
    key_N = len(key)
    key_array = []
    for i in range(key_N):
    for j in range(key_N):
        if key[i][j] == 0:
            key_array.append([i,j])
    return key_array

def solution(key, lock):
    

    # lock에 홈이 있는 좌표 저장
    lock_N = len(lock)
    lock_array = []
    for i in range(lock_N):
        for j in range(lock_N):
            if lock[i][j] == 0:
                lock_array.append([i,j])
                
    # 0도 에서 key에 돌기가 있는 좌표 저장    
    key_array = return_keyarray(key)
    if set(lock_array)-set(key_array) == set():
        return true
    else:
        for _ in range(1,N-1):
            key_array
        
    
    
    
                
    k = rotate_90(key)
    
    
    for(i = 0)
    
    
    
    
    
    

    
    return answer
