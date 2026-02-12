e500 = 0
e200 = 0
e100 = 0
e50 = 0
e20 = 0
e10 = 0
e5 = 0
e2 = 0
e1 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0
e, c = input().split()

e = int(e)
c = int(c)

if e > 0:

    if (e / 500) >= 1:
        e500 = int(e / 500)

    if e500 >= 1:
        e = e - (500 * e500)
        if (e / 200) >= 1:
            e200 = int(e / 200)
    else:
        if (e / 200) >= 1:
            e200 = int(e / 200)

    if e200 >= 1:
        e = e - (200 * e200)
        if (e / 100) >= 1:
            e100 = int(e / 100)
    else:
        if (e / 100) >= 1:
            e100 = int(e / 100)

    if e100 >= 1:
        e = e - (100 * e100)
        if (e / 50) >= 1:
            e50 = int(e / 50)
    else:
        if (e / 50) >= 1:
            e50 = int(e / 50)

    if e50 >= 1:
        e = e - (50 * e50)
        if (e / 20) >= 1:
            e20 = int(e / 20)
    else:
        if (e / 20) >= 1:
            e20 = int(e / 20)

    if e20 >= 1:
        e = e - (20 * e20)
        if (e / 10) >= 1:
            e10 = int(e / 10)
    else:
        if (e / 10) >= 1:
            e10 = int(e / 10)

    if e10 >= 1:
        e = e - (10 * e10)
        if (e / 5) >= 1:
            e5 = int(e / 5)
    else:
        if (e / 5) >= 1:
            e5 = int(e / 5)

    if e5 >= 1:
        e = e - (5 * e5)
        if (e / 2) >= 1:
            e2 = int(e / 2)
    else:
        if (e / 2) >= 1:
            e2 = int(e / 2)

    if e2 >= 1:
        e = e - (2 * e2)
        if (e / 1) >= 1:
            e1 = int(e / 1)
    else:
        if (e / 1) >= 1:
            e1 = int(e / 1)

if c > 0:

    if (c / 50) >= 1:
        c50 = int(c / 50)

    if c50 >= 1:
        c = c - (50 * c50)
        if (c / 20) >= 1:
            c20 = int(c / 20)
    else:
        if (c / 20) >= 1:
            c20 = int(c / 20)

    if c20 >= 1:
        c = c - (20 * c20)
        if (c / 10) >= 1:
            c10 = int(c / 10)
    else:
        if (c / 10) >= 1:
            c10 = int(c / 10)

    if c10 >= 1:
        c = c - (10 * c10)
        if (c / 5) >= 1:
            c5 = int(c / 5)
    else:
        if (c / 5) >= 1:
            c5 = int(c / 5)
    
    if c5 >= 1:
        c = c - (5 * c5)
        if (c / 2) >= 1:
            c2 = int(c / 2)
    else:
        if (c / 2) >= 1:
            c2 = int(c / 2)

    if c2 >= 1:
        c = c - (2 * c2)
        if (c / 1) >= 1:
            c1 = int(c / 1)
    else:
        if (c / 1) >= 1:
            c1 = int(c / 1)

print("Bitllets de 500 euros:", e500)
print("Bitllets de 200 euros:", e200)
print("Bitllets de 100 euros:", e100)
print("Bitllets de 50 euros:", e50)
print("Bitllets de 20 euros:", e20)
print("Bitllets de 10 euros:", e10)
print("Bitllets de 5 euros:", e5)
print("Monedes de 2 euros:", e2)
print("Monedes de 1 euro:", e1)
print("Monedes de 50 centims:", c50)
print("Monedes de 20 centims:", c20)
print("Monedes de 10 centims:", c10)
print("Monedes de 5 centims:", c5)
print("Monedes de 2 centims:", c2)
print("Monedes de 1 centim:", c1)