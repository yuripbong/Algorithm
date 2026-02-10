word = input()
word = list(word)

ABC2 = ['A', 'B', 'C']
DEF3 = ['D', 'E', 'F']
GHI4 = ['G', 'H', 'I']
JKL5 = ['J', 'K', 'L']
MNO6 = ['M', 'N', 'O']
PQRS7 = ['P', 'Q', 'R', 'S']
TUV8 = ['T', 'U', 'V']
WXYZ9 = ['W', 'X', 'Y', 'Z']

time = 0
for i in word:
    if i in ABC2:
        time += 3
    elif i in DEF3:
        time += 4
    elif i in GHI4:
        time += 5
    elif i in JKL5:
        time += 6
    elif i in MNO6:
        time += 7
    elif i in PQRS7:
        time += 8
    elif i in TUV8:
        time += 9
    elif i in WXYZ9:
        time += 10
        

print(time)