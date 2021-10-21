def reduce_form(n):
    if (n == 0):
        return 0
    divisible = True # assume x and y are divisible
    while(divisible):
        divisible = False
        if (n % 2 == 0):
            n = n/2
            divisible = True
        if (n % 3 == 0):
            n = n/3
            divisible = True
        if (n % 5 == 0):
            n = n/5
            divisible = True
    return n

def hcf(x, y): # returns the highest common factor
    if (x == y):
        return x
    if (x == 0 or y == 0):
        return 0
    res = 1

    divisible = True # assume x and y are divisible
    while(divisible):
        divisible = False
        if (x == 5 or x == 3 or x == 2 or y == 5 or y == 3 or y == 2):
            return int(res)
        if (x % 2 == 0 and y % 2 == 0):
            x = x/2
            y = y/2
            res = res * 2
            divisible = True
        if (x % 3 == 0 and y % 3 == 0):
            x = x/3
            y = y/3
            res = res * 3
            divisible = True
        if (x % 5 == 0 and y % 5 == 0):
            x = x/5
            y = y/5
            res = res * 5
            divisible = True
        if (x > y):
            rem = x % y # remainder
            rem = reduce_form(rem) # reduce the form of remainder
            if (rem == 0):
                res = res * y
                return res
            elif (rem == 1):
                divisible = False
                break
            elif (x % rem == 0 and y % rem == 0):
                x = x / rem
                y = y / rem
                res = res * rem
                divisible = True
        else:
            rem = y % x # remainder
            rem = reduce_form(rem) # reduce the form of remainder
            if (rem == 0):
                res = res * x
                return res
            elif (rem == 1):
                divisible = False
                break
            elif (y % rem == 0 and y % rem == 0):
                x = x / rem
                y = y / rem
                res = res * rem
                divisible = True

    return int(res)

# main
# function calling examples
##print(hcf(19, 38)) # 19
##print(hcf(6935, 6205)) # 365
##print(hcf(183,122)) # 61
##print(hcf(779, 58)) #1
##print(hcf(3895, 2337)) #779
##print(hcf(13243, 172159)) #13243
##print(hcf(39729, 26486)) #13243
##print(hcf(5491, 7429))#323

