rest = []

for i in range(10):
    num = int(input())
    rest.append(num % 42)
    
rest = set(rest)

print(len(rest))