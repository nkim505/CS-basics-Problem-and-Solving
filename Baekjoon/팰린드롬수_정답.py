while 1:
    n = input()
    if n != '0':
        rev = n[::-1]
        if n == rev:
            print('yes')
        else:
            print('no')
    else:
        break
