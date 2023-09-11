j = 2
flag = 0

for x in range(3, 101):
    while j <= x:
        if x % j == 0:
            flag+=1
        j+=1
    if flag == 1:
        print(x, " is prime")
    flag = 0
    j = 2

