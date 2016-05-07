'''

@author: Yanqing
'''

#partition : a sorted array of natural number
#c         : a natural number to be unioned to the partition.
def unionPartition(partition, c):
    setPartition = set(partition)
    setPartition.add(c)
    newPartition = list(setPartition)
    return sorted(newPartition)

def equipartitionYAxis(D, y):
    n = float(len(D))
    
    if n < y:
        raise ValueError('The number of the clumps cannot be larger than the points number')
    
    i = 1
    currRow = 1;
    desiredRowSize = n/y
    Q = [-1,0]
    currRowNum = 0
    while i <= n:
        j = i + 1
        while j <= n and D[j-1][1] == D[i-1][1]:
            j = j + 1
        S = j - i
        if currRowNum != 0 and abs(currRowNum + S - desiredRowSize) >= abs(currRowNum - desiredRowSize):
            currRow = currRow + 1;
            Q.append(0)
            desiredRowSize = (n - i + 1)/(y - currRow + 1)
            currRowNum = S
        else:
            currRowNum = currRowNum + S
        
        Q[currRow] = (D[i - 1][1])   
        i = i + S

    return Q

def GetRowIndex(y,Q):
    maxIndex = len(Q)
    minIndex = 0
    
    
    while (minIndex  + 1) < maxIndex:
        index = (maxIndex + minIndex)/2
        if y == Q[index]:
            return index
        elif y > Q[index]:
            minIndex = index
        else:
            maxIndex = index
    if  y == Q[minIndex]:
        return minIndex
    else:
        return maxIndex  
    
def GetColIndex(x,P):  
    return GetRowIndex(x,P)    

#D: points (x,y) set sorted by x-axis
#Q: partition of y-axis; Q is a array, each element of which is a y value of the boundary
def GetClumpsPartition(D, Q):
    P = [0,0]
    i = 1
    n = len(D)
    
    currCol = 1;
    currRow = GetRowIndex(D[i-1][1],Q)
    while i <= n:
        j = i + 1
        while (j <= n and (D[j-1][1] <= Q[currRow] and D[j-1][1] > Q[currRow-1])):
            j = j + 1
        if j > n:
            P[currCol] = n
            return P
        else: 
            P[currCol] = j - 1
        currCol = currCol + 1
        i = j 
        currRow = GetRowIndex(D[i-1][1],Q)  
        P.append(0) 

    return P


def GetSuperclumpsPartition(P, tildek):
    
    numOriginalClumps = len(P) - 1
    n = P[numOriginalClumps]
    
    if n < tildek:
        raise ValueError('The number of the clumps cannot be larger than the points number')
    
    i = 1
    currRol = 1;
    desiredRowSize = n/tildek
    rP = [0,P[i]]
    currRolNum = P[i] - P[i-1]
    while i < numOriginalClumps:
        S = P[i + 1] - P[i]
        if abs(currRolNum + S - desiredRowSize) >= abs(currRolNum - desiredRowSize):
            currRol = currRol + 1;
            rP.append(0)
            desiredRowSize = (n - P[i] + 1)/(tildek - currRol + 1)
            currRolNum = S
        else:
            currRolNum = currRolNum + S
        
        
        rP[currRol] = P[i + 1]  
        i = i + 1

    return rP
    
#D : points (x, y) sorted by x axis
def countNum(D, P, Q):   
    row = len(Q) - 1
    col = len(P) - 1
    count = [[0 for i in range(row + 1)] for j in range(col + 1)]
    
    n = 0
    i = 1
    for d in D:
        n = n + 1
        if n > P[i]:
            i = i + 1
        j = GetRowIndex(d[1],Q)
        count[i][j] = count[i][j] + 1
        
    sumCol = [sum(x) for x in count]    
    return count, sumCol 

def countNumFixedQ(xPartition, P, Q, count, sumCol):
    row = len(Q) - 1
    col = len(P) - 1
    resultCol = len(xPartition) - 1
    resultCount = [[0 for i in range(row + 1)] for j in range(resultCol + 1)]
    resultSumCol = [0 for i in range(resultCol + 1)]
    i = 1
#     resultSumCol[i] = sumCol[i] 
#     for j in range(1, row + 1):
#         resultCount[i][j] = count[i][j]
    start = GetColIndex(xPartition[i - 1], P)
    for c in range(start + 1, col + 1):
        if P[c] <= xPartition[i]:
            for j in range(1, row + 1):
                resultCount[i][j] =  resultCount[i][j] + count[c][j]
            resultSumCol[i] = resultSumCol[i] + sumCol[c]
        else:
            i = i + 1
            if i > resultCol:
                break
            for j in range(1,row + 1):
                resultCount[i][j] = count[c][j]
            resultSumCol[i] = sumCol[c]
                    
    return resultCount, resultSumCol

# def entropy(D,xPartition, Q, sumCol):   
#     col = len(xPartition) 
#     row = len(Q)  
#     countNum(D, xPartition, Q): 
#     totolNum = 
#     
#     for l in range(1, col):
#         for i in range(1,row):
#             sum = count
        
        
  
    
    
    



if __name__ == '__main__':

    
    

    count = [[0,0,0,0], [0,1,3,4],[0,2,5,8],[0,1,1,1],[0,2,3,4]]
    sumCol = [sum(x) for x in count]
    P = [0,8,23,26,35]
    Q = [-1,4,5,7]
    xPartition = [26,35]
    
    [dd, ddd] = countNumFixedQ(xPartition, P, Q, count, sumCol)
    print dd
    print ddd
    
#     Q = equipartitionYAxis(D,2)
# #     
# #     D = [(1,2),(3,4),(3,5)]
# #     Q = equipartitionYAxis(D,3)


