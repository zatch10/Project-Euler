i = 1
b = 3
def divider(i):
    for a in range(1,21):
        if i%a!=0:
            return False
        else:
            continue
    return True

while i < b:
    if divider(i):
        break
    else:
        i +=1
        b +=1

print(i)