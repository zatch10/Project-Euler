sum1 = 0
sum2 = 0
for i in range(1,101):
    sum1 = sum1 + i
    
sum1 = sum1*sum1

for i in range(1,101):
    sum2 = sum2 + i*i

ans = sum1 - sum2
print(ans)