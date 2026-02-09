h, m = map(int, input().split())
c = int(input()) # 필요한 시간

tmp = m+c

m = tmp % 60
    
h += (tmp // 60)

h %= 24

print(h, m)

