#368쪽 이진탐색 Q28 고정점 찾기
n = int(input())
array = list(map(int,input().split()))

def binary(array, n):  
    start = 0
    end = n-1
    while  start <= end:
        mid = (start+end)//2
        if mid == array[mid]:
            return(mid)
            break
        elif mid < array[mid]:
            end = mid - 1
            continue
        elif mid > array[mid]:
            start = mid + 1
    return(-1)

binary(array, n)
