from cantor import Cantor
from stack import Stack
from field import Field

# default infinite-infinite pairing

def_iip = Cantor

# selection

def select(x, y, iip = def_iip):
    if x == 0 and y == 0: return iip()
    elif x == 0: return Stack(y, 0)
    elif y == 0: return Stack(x, 1)
    else: return Field(x, y)

# composition operator

class Compose:
    
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
        (x, y) = self.pairings[0].split(n)
        l = [x]
        if self.arity > 2:
            for k in range(1, len(self.pairings)):
                (x, y) = self.pairings[k].split(y)
                l.append(x)
        l.append(y)
        return l

if __name__ == "__main__":
    p = Compose([2, 3, 4, 5])
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