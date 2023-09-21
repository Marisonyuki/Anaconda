c=0
b=1
print("Type in a number, i will check if it's simple")
a = int(input())
while c<=3:
    g = (a % b)
    if g == 0:
        print(b)
        c=c+1
        b=b+1
    if g>0:
        b=b+1
    if c == 2 and b > a:
        print("Simple number")
        time.sleep(5)
        break
    if c == 3 or a == 1:
        print("Not simple")
        break
