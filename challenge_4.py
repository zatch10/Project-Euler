palindrome=[]
checker=[]
def palindrome_check(num):
    val = str(num)
    if val == str(num)[::-1]:
        return True
    else:
        return False


for i in range(100,999):
     for j in range(100,i):
         num = j*i
         if palindrome_check(num):
             palindrome.append(num)
         else:
             continue     
print(max(palindrome))
