# 내 코드 
a, b = input().split()

a_rev = a[::-1]
b_rev = b[::-1]

result = max(a_rev, b_rev)
print(result)



# 시현님 코드
a, b = input().split()

new_a = a[::-1]
new_b = b[::-1]

if int(new_a) < int(new_b):
    print(int(new_b))
else:
    print(int(new_a))
