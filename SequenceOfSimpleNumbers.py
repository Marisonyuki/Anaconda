c=0
b=1
print("Type in first and last integer number of a sequence")
a = int(input())
h = int(input())
if a == 1:
    a = 2
for i in range(a, h+1):
    c=0
    b=1
    while c < 3:
        g = (i % b)
        if g == 0:
            c=c+1
            b=b+1
        if g>0:
            b=b+1
        if c == 2 and b > i:
            print(i)
            break
