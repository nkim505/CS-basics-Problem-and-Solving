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
