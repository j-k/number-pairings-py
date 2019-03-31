from test import tests

class Poto:
    
    @staticmethod
    def join(x, y):
       return (2 ** x) * (2 * y + 1) - 1
    
    @staticmethod
    def split(z):
        for i in range(0, z + 1):
            p = 2 ** i
            q = (z + 1) // p
            if q % 2 == 1:
                return (i, q // 2)
    
    @staticmethod
    def bounds(): return (0, 0, 0)

    @staticmethod
    def generate():
        z = 0
        while True:
            yield Poto.split(z)
            z += 1

if __name__ == "__main__":
    tests(Poto)


"""
# rest in piece: attempt to do a faster generate (possible?)
# stolen from:
# https://www.geeksforgeeks.org/check-n-divisible-power-2-without-using-arithmetic-operators/

# Python3 implementation to chech  
# whether n is divisible by pow(2, m) 
  
# function to chech whether n 
# is divisible by pow(2, m) 
def isDivBy2PowerM (n, m): 
      
    # if expression results to 0, then 
    # n is divisible by pow(2, m) 
    if (n & ((1 << m) - 1)) == 0: 
        return True
          
    # n is not divisible 
    return False

# function to find the minimal m
# for which n is divisible by pow(2, m)
def findM(n):
    for k in range(0, n//2):
        if isDivBy2PowerM(n, k): return k
    return None
"""