n, s, m = map(int, input().split())
v = list(map(int, input().split()))

v_list = [s]
cnt = 0

while cnt < n:
    print("current v_list:", v_list)
    bag = []
    for vol in v_list:
        a = vol + v[cnt]
        if a <= m and a >= 0:
            bag.append(a)
        b = vol - v[cnt]
        if b <= m and b >= 0:
            bag.append(b)

    v_list = bag
    cnt += 1
    

if len(v_list)==0:
    print(-1)
else:
    print(max(v_list))
    
    #메모리 문제 
