def solution(polynomial):
    answer = ''
    
    poly = polynomial.split(' ')
    print(poly)
    
    x_num = 0
    num = 0
    
    for i in range(0, len(poly), 2):
        if 'x' in poly[i]:
            if poly[i] == 'x':
                x_num += 1
            else:
                print(int(poly[i].split('x')[0]))
                x_num += int(poly[i].split('x')[0])
        else:
            num += int(poly[i])
    
    if x_num == 0:
        return str(num)
    if num == 0 and x_num == 1:
        return 'x'
    if num == 0:
        return str(x_num)+'x'
    if x_num == 1 and num != 0:
        return 'x + '+str(num)
    
    return str(x_num)+'x + '+str(num)