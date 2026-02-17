any = int(input())
num = 0

if int(any/100) == (any/100):
    any_div = str(int(any/100))
    if len(any_div) == 2:
        num = int(any_div)
        if int(num/4) == (num/4):
            print("YES")
        else:
            print("NO")
    else:
        num = int(any)
        if int(num/4) == (num/4):
            print("YES")
        else:
            print("NO")
else:
    num = int(any)
    if int(num/4) == (num/4):
        print("YES")
    else:
        print("NO")