n = int(input())

for i in range(n):
    s = input()
    print(s[0].upper(), end="")
    for j in range(1,len(s)):
        print(s[j], end="")
    print()
