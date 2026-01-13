def solution(s):
    
    s = list(s)
    print(s)
    
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        s[i] = s[i].lower()
        
    print(s)
    s = ''.join(s)
    print(s)
    
    s = s.title()
    print(s)
    
    for i in range(len(s)):
        if s[i].isdigit():
            s = s.replace(s[i+1], s[i+1].lower())

    return s