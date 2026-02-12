h = [0]
m = [0]
s = [0]
hms = []

hora_del_dia = input().split()

h1 = int(hora_del_dia[0])

if int(hora_del_dia[1]) == 59:
    h1 = h1 + 1
    m1 = 0
else:
    m1 = int(hora_del_dia[1])

if int(hora_del_dia[2]) == 59:
    m1 = m1 + 1
    s1 = 0
else:
    s1 = int(hora_del_dia[2]) + 1

if len(str(h1)) == 1:
    h.append(h1)
else:
    h = h1

if len(str(m1)) == 1:
    m.append(m1)
else:
    m = m1

if len(str(s1)) == 1:
    s.append(s1)
else:
    s = s1

h = str(h)
m = str(m)
s = str(s)

hms.append(h)
hms.append(m)
hms.append(s)
output = ':'.join(hms)

print(output)