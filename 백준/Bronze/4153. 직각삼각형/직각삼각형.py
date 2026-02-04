while True:
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    
    if a == 0 and b == 0 and c == 0:
        break
    
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    
    s = sorted(l)
    if (s[0]**2 + s[1]**2) == s[2]**2:
        print('right')
    else:
        print('wrong')
    
    
    