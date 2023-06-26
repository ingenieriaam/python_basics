####################################################
#
import numpy as np
def return_different(n1, n2, n3):
    if n1+n2+n3 >15:
        return max(n1, n2, n3)
    elif n1+n2+n3 <10:
        return min(n1, n2, n3)
    else:
        return np.median([n1, n2, n3])
    
print(return_different(1,2,3))
print(return_different(10,12,3))
print(return_different(1,9,3))