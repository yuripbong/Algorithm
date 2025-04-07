import string

s = input()
alphabet = list(string.ascii_lowercase)
answer = [0] * len(alphabet)

for i in range(len(s)):
    for j in range(len(alphabet)):
        if s[i] == alphabet[j]:
            answer[j] += 1
            
for i in range(len(answer)):
    print(answer[i], end=" ")
