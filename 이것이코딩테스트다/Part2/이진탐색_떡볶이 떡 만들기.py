# 떡볶이 떡 만들기
n, m = list(map(int, input().split())) #떡의 갯수 4
array = list(map(int, input().split())) 19 15 10 17

array.sort()

start = 0
end = max(array) #가장 긴 떡의 길이가 end 점이 된다

result = 0
while start <= end:
    total = 0 # 절단기 바뀔 때마다 리셋
    mid = (start + end)//2
    
    for x in array:
    # 잘랐을 때 떡의 양을 계산
        if x > mid:
            total += x - mid
    if total > m:
        end = mid - 1
        
    else:
        result = mid # 최대한 덜 잘랐을 때를 return해야해서, result 값들을 일단 계속해서 기록
        start = mid + 1

print(result)
