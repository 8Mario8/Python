a1, b1, a2, b2 = input().split()

i1 = [a1, b1]
i2 = [a2, b2]

output = []

if a1 <= b1 and a2 <= b2:
    if i1[0] in i2:
        output = i1
        if i1[1] in i2:
            output.append(i1[1])
        else:
            output.append(i1[0])
    else:
        output = []

print(output)

