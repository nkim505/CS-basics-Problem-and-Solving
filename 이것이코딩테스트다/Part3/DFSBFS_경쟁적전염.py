# https://www.acmicpc.net/problem/18405
# 틀린 풀이
n, k = map(int, input().split())

array = []
for i in range(n):
    tmp = list(map(int, input().split()))
    array.append(tmp)

s, x, y = map(int, input().split())



dx = [-1, 0 , 1, 0] # 상 우 하 좌
dy = [0 , 1, 0, -1]
  
def virus(x, y, virus_code): 
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

      #상하좌우로 바이러스가 증식함
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
          if array[nx][ny] == 0:
              array[nx][ny] = virus_code 


def check_virus_location(array):
    bins = [(999,999)]*(k+1)
    for i in range(n):
        for j in range(n):
            if array[i][j] != 0:
                virus_code = array[i][j]
                bins[virus_code] = (i,j)
    return bins


time  = 0 
while time < s :
    bins = check_virus_location(array)
    for virus_code, i in enumerate(bins):
        if i[0] == 999:
            continue
        else:
            virus(i[0], i[1], virus_code)
    time += 1

print(array[x-1][y-1])


# 다시 
