
def BubbleSort(x:list,reverse=False):
    ''' Bubble sort, 
    time complexity O(n^2)
    
    If reverse is true then it will print the list in 
    descending order
    '''
   
    for i in range(len(x)-1):
        for j in range(len(x)-1-i):
            if not reverse:
                if x[j]>x[j+1]:
                    x[j], x[j+1]=x[j+1], x[j]
            else:
                if x[j]<x[j+1]:
                    x[j], x[j+1]=x[j+1], x[j]
    return x
   
   

def SelectionSort(x:list):
    '''Time complexity O(n^2)'''
    for i in range(len(x)):
        smol=i
        for j in range(i+1,len(x)):
            if x[smol]>x[j]:
                smol=j
        x[i],x[smol]=x[smol],x[i]
    return x



def InsertionSort(x):
    '''Time complexity O(n^2)
    In this sorting algo the array is divided into 2 subarrays
    1. sorted subarrays (left)
    2. unsorted subarrays (right)
    
    key is the 1st element of the unsorted subarray
    if the last element of the sorted subarray is greater
    than the key then swap them. 

    do this untill you find an element that is lesser than key
    then break the loop
    
    '''
    for j in range(1,len(x)):
        key=x[j]
        i=j-1
        while i>=0 and x[i]>key:
            x[i+1]=x[i]
            i-=1
        x[i+1]=key
    return x

def MergeSort(a):
    '''
    Time complexity : O(N log N)
    divide and conquere rule
    
    '''

    size=len(a)
    if size<2:
        return a
    mid=size//2
    l=a[:mid]
    r=a[mid:]
    l=MergeSort(l)
    r=MergeSort(r)
    i,j=0,0
    b=[]
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            b.append(l[i])
            i+=1
        else:
            b.append(r[j])
            j+=1

    while i<len(l):
        b.append(l[i])
        i+=1
        
    while j<len(r):
        b.append(r[j])
        j+=1
        
    return b



def QuickSort(a):
    pass


