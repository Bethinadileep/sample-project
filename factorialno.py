def factorialno(num):
    if(num==0 or num==1):
        return num
    fact=1
    for i in range(2,num+1):
        fact=fact*i
    return fact
print(factorialno(5))
