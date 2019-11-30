pre = ""
pos = 0
a = ["flower","flow","flight"]
condition = True

while condition:
    if len(set([x[pos] for x in a])) == 1:
        pre += a[0][pos]
    else:
        break
    pos += 1

print(pre)