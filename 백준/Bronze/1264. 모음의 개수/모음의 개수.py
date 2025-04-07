mo = ['a', 'e', 'i', 'o', 'u']
while True:
    s = input()
    answer = 0
    if s == "#":
        break
    else:
        s = s.lower()
        for i in range(len(s)):
            for j in range(len(mo)):
                if s[i] == mo[j]:
                    answer += 1
    print(answer)
                    
        