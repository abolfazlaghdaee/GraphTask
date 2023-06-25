import numpy as np


def WPolythiophene(p):

    # base matrix of polythiophene
    base = np.array([[0, 1, 2, 3, 3, 2, 4],
                     [1, 0, 1, 2, 2, 1, 3],
                     [2, 1, 0, 1, 2, 2, 3],
                     [3, 2, 1, 0, 1, 2, 2],
                     [3, 2, 2, 1, 0, 1, 1],
                     [2, 1, 2, 2, 1, 0, 2],
                     [4, 3, 3, 2, 1, 2, 0]])
    
    # complement matrix of base matrix
    complement = np.array([[0, 1, 2, 2, 3],
                           [1, 0, 1, 2, 2],
                           [2, 1, 0, 1, 1],
                           [2, 2, 1, 0, 2],
                           [3, 2, 1, 2 ,0]])
    
    
    n= p*5 +2 #number of nodes 

    
    j = int((n-7) / 5)  # calculate of number of repeats
    
    
    new = base 
    for i in range(j):  
        base = new
        
        
         
        
        a = base.shape[0]
        new = np.column_stack((new, base[:,a -1] +1)) # extend columns of new matrix
        new = np.column_stack((new, base[:,a -1] +2))
        new = np.column_stack((new, base[:,a -1] +2))
        new = np.column_stack((new, base[:,a -1] +1))
        new = np.column_stack((new, base[:,a -1] +3))
        
        

        for k in range(5):
            base = np.column_stack((base, np.zeros(a)))  #extend columns of base matrix



        new = np.vstack((new, new[a-1,:] +1)) #extend row of new matrix
        new = np.vstack((new, new[a-1,:] +2))
        new = np.vstack((new, new[a-1,:] +2))
        new = np.vstack((new, new[a-1,:] +1))
        new = np.vstack((new, new[a-1,:] +3))

        b = new.shape[0]  - 1   
        new[b -4: , b - 4:] =0  
        
        


        C_col= complement.shape[1]
        
        
        # generate new compelement matrix by dimention of new matrix 

        for i in range(100): 

            if complement.shape[0] == new.shape[0] :
                break
            complement= np.insert(complement, 0, np.zeros(C_col), axis=0)



        C_row = complement.shape[0]   

        for i in range(100):

            if complement.shape[1] == new.shape[1] :
                 break
            complement= np.insert(complement, 0, np.zeros(C_row), axis=1)
            
            
        new = new + complement
            

        
    return new, new.sum()/2




p = int(input("Enter the number of PT: "))
print(WPolythiophene(p))
    
    