from random import randint

a=0
while a>-1:
    print("guess the number from 1 to 10")
    i = randint(1, 10)
    s = int(input())
    if i==s:
        print("You won!!!")
        a = a+1
        print("Wins = ", a)
        s = 0
    else:
        a = -1
