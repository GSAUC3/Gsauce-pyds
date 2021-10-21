


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