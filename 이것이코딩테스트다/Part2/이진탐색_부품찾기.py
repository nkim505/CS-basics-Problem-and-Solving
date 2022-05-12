# array  = [2 3 7 8 9] , target = 5 , 0, n-1
# array꼭 spot 
def binary_search(array, target, start, end):
    while start  <= end :
        mid = (start+end)//2 # 소수점 버림
        if array[mid] == target:
            return mid
                    
				elif array[mid]  > target:
            end = mid - 1 
        else:
					start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())

x = list(map(int, input().split())) # 5 7 9

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end =' ')
    else:
        print('no', end = ' ')
