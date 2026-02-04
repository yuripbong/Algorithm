import sys

n = int(sys.stdin.readline())
size_counts = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

t_order = 0
for count in size_counts:
    if count == 0:
        continue
    elif count <= t:
        t_order += 1
    else:
        t_order += (count // t)
        if (count % t) != 0:
            t_order += 1

p1 = n // p
p2 = n % p

print(t_order)
print(p1, p2)
