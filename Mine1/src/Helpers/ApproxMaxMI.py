'''

@author: Yanqing
'''
from Helpers import *

# Require: D is a set of ordered pairs sorted in increasing order by x-value
# Require: Q is a y-axis partition of D
# Require: x is an integer greater than 1
def ApproxOptimizeXAxis(D, Q, x, tildek):
    c = GetClumpsPartition(D, Q)
    k = len(c) - 1;
    if k > tildek:
        c = GetSuperclumpsPartition(c, tildek)
        numClumps= tildek
    P = [[[] for x in range(1, x + 1)] for y in range(1, k + 1)]
    I = [[0 for x in range(1, x + 1)] for y in range(1, k + 1)]
    
    [count,sumCol] = countNum(D, c, Q)
     
    #caculate H(Q), which means only have one row so P = [0,P[-1]] 
    [subCount,subSumCol] = countNumFixedQ([0,c[-1]], P, count,sumCol)
    HQ = entropy(subCount, subSumCol)   
    #Find the optimal partitions of size 2
    
    for t in range(2,k):
        maxDiff = float('-inf')
        #Find s \in {1,...,t} maximizing H(<c0,cs,ct>)- H(<c0,cs,cti>,Q).
        c0_ct = [c[0],c[t]]
        for s in range(1, t):
            c0_cs_ct = unionPartition(c0_ct, c[s])
            #caculate H(P), which means only have one row so Q = [-1,Q[-1]]
            
            [subCount,subSumCol] = countNum(D, c0_cs_ct, [-1,Q[-1]])
            HPt2 = entropy(subCount, subSumCol)
            
            #caculate H(P,Q)
            [subCount,subSumCol] = countNum(D, c0_cs_ct, Q)
            HPQ = entropy(subCount, subSumCol)
            
            diffEntropy = HPt2 -HPQ
            if diffEntropy > maxDiff:
                maxDiff = diffEntropy
                P[t][2] = c0_cs_ct
                I[t][2] = HQ + diffEntropy
                
    #Inductively build the rest of the table of optimal partitions
    for l in range(3, x + 1):
        for t in range(l, k):
            maxDiff = float('-inf')
            for s in range(l - 1, t):
                firstPart = (c[s]/c[t]) * (I[s][l-1] - HQ)
                cs_ct = [c[s],c[t]]
                [count,sumCol] = countNum(D, cs_ct, Q)
                HPQ = entropy(count, sumCol)
                secondPart = ((c[t] - c[s])/c[t]) * HPQ 
                
                if (firstPart - secondPart) > maxDiff:
                    maxDiff = firstPart - secondPart
                    P[t][l] = unionPartition(P[t][l-1], c[t])
                    
                    #caculate HPtl, which means only have one row so Q = [-1,Q[-1]]
                    
                    [subCount,subSumCol] = countNum(D, P[t][l], [-1,Q[-1]])
                    HPtl = entropy(subCount, subSumCol)
                    I[t][l] = HQ + HPtl + unionPartition(P[t][l-1], c[t])
                    
              
        
    
    

if __name__ == '__main__':
    pass