# list.remove()의 시간 복잡도는 O(N)
# 대신 쓰는 방법

a = [1,2,3,4,5]
remove_set = {3,4}

#remove_set에 포함되지 않은 값만 저장
result = [i for i in a if i not in remove_set]
print(result)
