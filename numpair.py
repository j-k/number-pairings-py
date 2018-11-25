# Copyright (C) 2018 Jens Kubacki - All Rights Reserved
# see license file

"""
// this modules implements some binary pairings
// - these are objects like {join:...,split:...,bounds:...},
// - where
//   join: ( x, y ) -> z
//     maps the z ( x, y ) uniquely to z
//   split: ( z ) -> ( x, y ) is the inverse of z
//   and bounds are the bounds of the two inputs (bound[0], bound[1])
//     and the output (bound[2])
// - a bound of 0 means unbounded, otherwise the bound is the maximum value plus one
// - all numbers are assumed to be positive integers including zero
// - there are also half-pairings for commutative relations
"""

import math
import isqrt.isqrt as isqrt

# triangle numbers
def tn(x):
    return x * (x + 1) // 2 

# triangle root
def tr(x):
    return (isqrt(1 + x * 8) - 1) // 2

# excess over the last triangle number
def ext(x):
    return x - tn(tr(x))

class Cantor:

    @staticmethod
    def join(x, y):
        return tn(x + y) + y

    @staticmethod
    def split(z):
        t = tr(z)
        return [
          ( t * ( t + 3 ) // 2 ) - z,
          z - ( ( t * ( t + 1 ) ) // 2 )
        ]

    @staticmethod
    def bounds():
      return [0, 0, 0]

class Elegant:
   
    @staticmethod
    def join(x, y):
        if y >= x:
            return y * (y + 1) + x
        else:
            return x * x + y
    
    @staticmethod
    def split(z):
      sq_z = isqrt(z)
      if (sq_z * sq_z) > z:
          sq_z = sq_z - 1
      t = z - sq_z * sq_z
      if t < sq_z: return [ sq_z, t ]
      else: return [ t - sq_z, sq_z ]
    
    @staticmethod
    def bounds():
        return [0, 0, 0]

class Poto:
    
    @staticmethod
    def join(x, y):
       return (2 ** x) * (2 * y + 1) - 1
    
    @staticmethod
    def split(z):
        _z = z + 1
        for i in range(0, _z):
            x = i
            p = 2 ** x
            q = _z // p
            if q % 2 == 1:
                return [x, q // 2]
    
    @staticmethod
    def bounds(): return [ 0, 0, 0 ]


# half pairing (only x <= y pairs)

class Half:

    @staticmethod
    def join(x, y): return tn(max(x, y)) + min(x, y)
    
    @staticmethod
    def split(z): return [ ext( z ), tr( z ) ]
    
    @staticmethod
    def bounds(): return [ 0, 0, 0 ]


# finite field (matrix) of two dimensions

class Field:
  
    def __init__(self, sx, sy):
        self.sx = sx
        self.sy = sy
        self.sz = sx * sy
    
    def join(self, x, y):
        if x < self.sx and y < self.sy:
            return self.sx * y + x % self.sx
    
    def split(self, z):
        if z < self.sz:
            return [ z % self.sx, z // self.sx ]
    
    def bounds(self):
      return [ self.sx, self.sy, self.sz ]

# x (y) is infinite and y (x) is finite
# s: size in the finite axis

class Stack:
  
    def __init__(self, s, xy=0):
        self.s = s
        self.xy = xy

    def join(self, x, y):
        if self.xy == 0:
            if y < self.s:
                return y % self.s + self.s * x
        else:
            if x < self.s:
                return x % self.s + self.s * y
  
    def split(self, z):
        if self.xy == 0:
            return [ z // self.s, z % self.s ]
        else:
            return [ z % self.s, z // self.s ]

    def bounds(self):
        if self.xy == 0:
            return [ 0, self.s, 0 ]
        else:
            return [ self.s, 0, 0 ]

# default infinite-infinite pairing

def_iip = Cantor

# selection

def select(x, y, iip = def_iip):
    if x == 0 and y == 0: return iip()
    elif x == 0: return Stack(y, 0)
    elif y == 0: return Stack(x, 1)
    else: return Field(x, y)

# composition operator

class Composition():
    
    def __init__(self, l, iip = def_iip ):
        
        self.arity = len(l)
        self.pairings = [ select( l[self.arity-2], l[self.arity-1], iip ) ]
    
        if self.arity > 2:
            for i in range(self.arity-3, -1, -1):
                new_pairing = select( l[i], self.pairings[0].bounds()[2], iip )
                self.pairings = [ new_pairing ] + self.pairings
        
        self.bounds = l + [ self.pairings[0].bounds()[2] ]
    
    def join(self, l):
        k = len(l)
        if k != self.arity: return
        for i in range(0, self.arity):
            if l[i] >= self.bounds[i] and self.bounds[i] > 0:
                return
        n = self.pairings[k-2].join(l[k-2], l[k-1])
        if self.arity > 2:
            for i in range(k-3, -1, -1):
                n = self.pairings[i].join(l[i], n)
        return n
    
    def split(self, n):
        if n >= self.bounds[self.arity] and self.bounds[self.arity] > 0:
            return
        [x, y] = self.pairings[0].split(n)
        l = [x]
        if self.arity > 2:
            for k in range(1, len(self.pairings)):
                [ x, y ] = self.pairings[k].split( y )
                l.append(x)
        l.append(y)
        return l

def tests():
    
    p = Cantor()
    z = p.join(10, 34)
    print(z)
    assert z == 1024
    x, y = p.split(1024)
    print(x, y)
    assert x, y == (10, 34)
    
    p = Elegant()
    z = p.join(10, 34)
    print(z)
    assert z == 1200
    x, y = p.split(1200)
    print(x, y)
    assert x, y == (10, 34)

    p = Poto()
    z = p.join(10, 34)
    print(z)
    assert z == 70655
    x, y = p.split(70655)
    print(x, y)
    assert x, y == (10, 34)

    p = Half()
    u = p.join(10, 34)
    v = p.join(34, 10)
    print(u)
    assert u == 605
    assert u == v
    x, y = p.split( 605 )
    print(x, y)
    assert x, y == (10, 34)

    p = Field(2, 3)
    z = p.join(1, 2)
    print(z)
    assert z == 5
    z = p.join(2, 2)
    print(z)
    assert z == None
    x, y = p.split( 5 )
    print(x, y)
    assert x, y == (1, 2)

    p = Stack(5, 0)
    z = p.join(2, 4)
    print(z)
    assert z == 14
    z = p.join(2, 5)
    print(z)
    assert z == None
    x, y = p.split(14)
    print(x, y)
    assert x, y == (2, 4)

    p = Composition([2, 3, 4, 5])
    xyz = [0, 1, 2, 3]
    z = p.join(xyz)
    print(z)
    assert z == 86
    xyz = p.split( 86 )
    print(xyz)
    assert xyz == [0, 1, 2, 3]
    assert p.join([1, 0, 0, 0]) == 1
    assert p.join([ 0, 1, 0, 0]) == 2
    assert p.join([ 0, 0, 1, 0]) == 6
    assert p.join([ 0, 0, 0, 1 ]) == 24

if __name__ == "__main__":
    tests()
