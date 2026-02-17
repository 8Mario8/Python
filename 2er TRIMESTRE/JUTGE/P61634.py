any = input()
any = any.split()
num = []

if any[2]:
    if any[2] == any[3] and any[2] == 0:
        num = [any[0], any[1]]
        num = str(num)
        num = int(num)
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