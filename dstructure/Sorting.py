
def BubbleSort(x:list):
    ''' Bubble sort, 
    time complexity O(n^2)
    '''
    for i in range(len(x)-1):
        for j in range(len(x)-1-i):
            if x[j]>x[j+1]:
                x[j], x[j+1]=x[j+1], x[j]

    return x


def SelectionSort(x:list):
    '''Time complexity O(n^2)'''
    for i in range(len(x)):
        smol=i
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                smol=j
        x[i],x[smol]=x[smol],x[i]
    return x



def InsertionSort(x):
    pass   