#no 1 rekursi
def anu(n):
    if (n==0):
        return 0
    else:
        return anu (n-1)+2
print("No. 1 Rekursi")
print("Hasil = ",anu(4))
print("==============")

#no2 rekursi
def p(a,n):
    if (n==0):
        return 1
    else:
        return a*p(a,n-1)
print("NO. 2 Rekursi")
print("Hasil = ",p(3,4))
print("==============")

#no3 Rekursi
def R(n):
    if (n==1):
        return -7
    else:
        return R(n-1)+12
print("No. 3 Rekursi")
print("Hasil = ",R(29))
print("==============")

#no4 soal sendiri
def g(b,c):
    if (c==1):
        return 2
    else:
        return g(b,c-1)-2
print("No. 4 Rekursi Soal Sendiri")
print("Hasil = ",g(6,8))
print("==============")
