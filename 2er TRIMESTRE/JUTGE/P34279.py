h = [0]
m = [0]
s = [0]
h1 = 0
m1 = 0
s1 = 0
hms = []

hora_del_dia = input().split()

h1 = int(hora_del_dia[0])

if int(hora_del_dia[2]) == 59:
    m1 = m1 + 1
    s1 = 0
else:
    s1 = int(hora_del_dia[2]) + 1

if int(hora_del_dia[1]) == 59:
    h1 = h1 + 1
    m1 = 0
elif int(hora_del_dia[1]) == 60:
    h1 = h1 + 1
    m1 = 0
else:
    m1 = int(hora_del_dia[1])

if len(str(h1)) == 1:
    h.append(h1)
    h = list(map(str, h))
    h = "".join(h)
else:
    h = h1
    h = str(h)

if len(str(m1)) == 1:
    m.append(m1)
    m = list(map(str, m))
    m = "".join(m)
else:
    m = m1
    m = str(m)

if len(str(s1)) == 1:
    s.append(s1)
    s = list(map(str, s))
    s = "".join(s)
else:
    s = s1
    s = str(s)

hms.append(h)
hms.append(m)
hms.append(s)
output = ":".join(hms)

print(output)