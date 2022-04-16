''' 2차원 리스트 초기화 하기 '''

# n,m 크기의 2차원 리스트 초기화할 때 반드시 리스트 컴프리핸션을 이용한다.
n=3
m=4
array= [[0]*m for _ in range(n)]
print(array)


# 잘못된 예
n=3
m=4
array= [[0]*m]*n
print(array)
array[1][1] = 5
print(array)

# for _ 언더바의 역할: 반복을 위한 변수 i 무시하고 순서만 돌리고 싶을 때.
