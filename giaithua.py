def giaithua1(x):
    if x==1:
        return 1
    else:
        return x*giaithua1(x-1)
def giaithua2(x):
    X=[]
    dem=0
    X.append(1)
    for i in range(2,x+1):
        a=X[dem]*i
        X.append(a)
        dem=dem+1
    return X[dem-1]
if __name__=="__main__":
    x=int(input("Nhap x="))
    print ("Cach de quy:")
    print (giaithua1(x))
    print ("Cach quy hoach dong:")
    print (giaithua2(x+1))