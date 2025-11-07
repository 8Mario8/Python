password="a1e4jk"
vocales="aeiouAEIOU"
total=0
total_vocales=0
for i in password:
    if i.isnumeric():
        total=total+int(i)
    if i in vocales:
        total_vocales=total_vocales+1
print(total)
print(total_vocales)