'''

@author: Yanqing
'''
from Helpers.Helpers import PerpD
from Helpers.ApproxMaxMI import ApproxMaxMI
import numpy as np

class MINE(object):
    '''
    classdocs
    '''


    def __init__(self, D):
        '''
        Constructor
        '''
        self.D = D
        self.DPerp = PerpD(D)

    def ApproxCharacteristicMatrix(self, B, c):  
        if B <= 3:
            print "Parameter B should be greater than 3!"
            return None
               
        if c < 1:
            print "Parameter B should be greater than 1!"
            return None
        
        Ixy = float('-inf')
        for y in range(2, B/2 + 1):
            x = B/y
            I = ApproxMaxMI(self.D,x,y,c*x)
            IPerp = ApproxMaxMI(self.DPerp,x,y,c*x)
            maxI_index  = np.argmax(I)
            maxIPerp_index = np.argmax(IPerp)
            
            if I[maxI_index] > IPerp[maxIPerp_index]:
                tempMaxI = I[maxI_index]
                max_x = maxI_index
            else:
                tempMaxI = IPerp[maxIPerp_index] 
                max_x = maxIPerp_index 
                
            if tempMaxI > Ixy:
                Ixy = tempMaxI
                Mxy = Ixy/np.log(min(max_x,y))
                    
        return Mxy        
    
    
if __name__ == '__main__':

    D = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)]
    n = len(D)
    B = int(n**0.9)
    c = 1.6
    M = MINE(D)
    print M.ApproxCharacteristicMatrix(B, c)
            
            
             
            

    
        
     
        