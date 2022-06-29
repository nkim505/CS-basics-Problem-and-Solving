#0 4 2 5 6

lst = list(map(int, input().split()))

sums = 0

for i in lst:
    sums += (i**2)
    
_, result = divmod(sums, 10)

print(result)



# 처음에 틀릴 때 i의 제곱을 i^2 라고 해서 틀림..
