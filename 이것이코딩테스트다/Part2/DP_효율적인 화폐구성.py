# 228page
# 정수 n, m 입력 받기
n, m = map(int, input().split())

#n개의 화폐 단위 정보 입력 받기
array = []
for i in range(n):
  array.append(int(input))
  
#한 번 계산된 결과를 저장하기 위한 DP테이블 초기화ㅣ

d = [10001] * (m+1) # 0에서 m까지

#보텀업 진행
d[0] = 0 # 0을 만드는 방법은 0이니까

for i in range(n) : # 화폐 단위 한 개씩 다 돈다 (이중 for 된다)
  for j in range(array[i], m+1):
    if d[j - array[i]] = ! 10001 : # i-k원을 만드는 방법이 존재하면
      d[j] = min(d[j], d[j-array[i]] +1)
      
if d[m] == 10001:
  print(-1)
else:
  print(d[m])
