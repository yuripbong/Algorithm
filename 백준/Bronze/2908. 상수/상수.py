a, b = input().split()

a = a[::-1]
a = int(''.join(a))

b = b[::-1]
b = int(''.join(b))

if a > b:
    print(a)
else:
    print(b)
