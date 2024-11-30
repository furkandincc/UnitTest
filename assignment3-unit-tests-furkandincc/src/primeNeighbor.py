'''
Created by Neda Topuz
Modified by Furkan Dinç

'''

def primeNeighbor(upperBound):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
       
    if not isinstance(upperBound, int):
        return None

    for num in range(upperBound - 1, 1, -1): 
        if is_prime(num):
            return num

    return None  

