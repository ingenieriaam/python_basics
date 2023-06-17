####################################################
#

def two_consecutive_zeros(*args):
    counter = 0
    for i in args:
        if counter == 2:
            return True
        if i == 0:
            counter += 1
        else:
            counter = 0
    return False

print(two_consecutive_zeros(5,6,1,0,0,9,3,5))
print(two_consecutive_zeros(6,0,5,1,0,3,0,1))
