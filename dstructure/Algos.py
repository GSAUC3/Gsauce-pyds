


def seiveprimes(n):
    '''n -> number of elements
        Seive of eratosthenes implementation'''
    isprimearray=[False,False]+[True for i in range(n-1)]
    i=2
    while i*i <=n:
        j=2*i
        while j<=n:
            isprimearray[j]=False
            j+=i
        i+=1

    return isprimearray

def euclidGCD(x: int,y: int):
    if y==0:
        return x
    return euclidGCD(y,x%y)


def powermodulo(a,b,n):
    '''returns (a^b)%n'''
    ans=1
    while b>0:
        if (b&1)!=0:
            ans=(ans* a%n)%n
        a=(a%n * a%n)%n
        b=b>>1
    return ans
    
