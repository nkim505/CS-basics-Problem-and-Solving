#시간초과

import sys
input = sys.stdin.readline

n = int(input())
music_lst = list(map(int, input().split()))
q = int(input())
ranges = []
for _ in range(q):
    x, y = map(int, input().split())
    ranges.append((x, y))
    
results = []

for x, y in ranges:
    lst = music_lst[x-1:y]
    m = len(lst)
    cnt_miss = 0
    for idx in range(m-1): # m-1:마지막 제외하고
        if lst[idx]>lst[idx+1]:
            cnt_miss += 1
            
    result = m - cnt_miss
    results.append(result)

for i in range(q):
    print(results[i], end = "\n")
