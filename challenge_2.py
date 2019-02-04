#Even Fibonacci numbers#
fibb1 = 1
fibb2 = 2
sum = 2
limit = 0
count = 0
while limit<=4000000:
    fibb2 += fibb1
    fibb1 = fibb2 - fibb1
    limit = fibb1
    count += 1

fibb1 = 1
fibb2 = 2
for i in range(0,count):
    fibb2 += fibb1
    fibb1 = fibb2 - fibb1
    if fibb2%2 == 0:
        sum += fibb2
    i += 1
print(sum)
    

