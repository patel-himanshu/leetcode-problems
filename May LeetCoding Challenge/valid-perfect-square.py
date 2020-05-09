# Question: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/

def isPerfectSquare(num):
    n = str(num)
    l = len(n)
    if l%2 == 1:
        n = '0'+n
        l += 1
    
    divisor = ''
    dividend = ''
    
    for i in range(0, l, 2):
        dividend += n[i: i+2]
        
        dnd_int = int(dividend)
        for j in range(0,11):
            dvr_int = int(divisor + str(j))
            res = dnd_int - (dvr_int * j)
            
            # Previous value was the one to be placed in blank of divisor
            if res < 0 or j == 10:
                sub = int(divisor + str(j-1)) * (j-1)
                res = dnd_int - sub
                divisor = str(int(divisor + str(j-1)) + int(j-1))
                dividend = str(int(dividend) - sub)
                break
                
    if int(dividend) == 0:
        return True
    else:
        return False

print('True cases')
for i in [0,1,4,9,16,25,81,225]:
    print(isPerfectSquare(i))
print('False Cases')
for j in [2,3,8,10,99]:
    print(isPerfectSquare(j))