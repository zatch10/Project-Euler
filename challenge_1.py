#multiples of 3 and 5"#
var_1 = 0
var_2 = 0
var_3 = 0
num_3 = 0
num_5 = 0
num_3_5 = 0

for i in range(0,1000):
        if num_3%3 == 0:
            var_1 += num_3
        if num_5%5 == 0:
            var_2 += num_5
        if num_3_5%3 == 0 and num_3_5%5 == 0:
            var_3 += num_3_5
        num_3_5 += 1
        num_3 += 1
        num_5 += 1
        i += 1
        
        
print(var_1 + var_2 - var_3)
