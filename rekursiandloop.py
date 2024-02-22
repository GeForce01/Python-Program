#no1 loop
def anu(n):
    result = 0

    for i in range(1, (n-1)+2):
        result = result + 2

    return result
print("No. 1 Loop")
print("Hasil",anu(4))
print("==============")

#no2 loop
def p(a,n):
    if (n==0):
        return 1
    else:
        return a
    for i in range(1,a,n):
        return a*(a,n-1)
print("No. 2 Loop")
print("Hasil",p(3,4))
print("==============")

#no3 loop
def r(n):
    result=-7

    for i in range(1,(n-1)+12):
        result=result + i
    return result
print("No. 3 loop")
print("Hasil = ",r(29))
print("==============")