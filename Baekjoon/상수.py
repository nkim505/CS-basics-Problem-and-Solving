a, b = input().split()

a_rev = a[::-1]
b_rev = b[::-1]

result = max(a_rev, b_rev)
print(result)
