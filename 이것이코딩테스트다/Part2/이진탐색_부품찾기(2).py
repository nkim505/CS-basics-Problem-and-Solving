from time import time
n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
x = list(map(int, input().split())) # 5 7 9

start = time()

for item in x:
    if array.count(item) == 0:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')

time = time()

print("\n 소요 시간 : {}".format(time - start
#소요 시간 : 0.0010018348693847656 (확실히 이진탐색이 빠름)
