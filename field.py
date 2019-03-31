from test import tests

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
            return (z % self.sx, z // self.sx)
    
    def bounds(self):
      return (self.sx, self.sy, self.sz)

    def generate(self):
        def _generate(sx=self.sx, sy=self.sy):
            u, v = 0, 0
            while u < sx and v < sy:
                yield u, v
                if u < sx - 1: u += 1
                else: v += 1; u = 0
        return _generate()

if __name__ == "__main__":
    p = Field(6, 4)
    a, b = 2, 3
    z = p.join(a, b)
    print(f"join({a}, {b}) ->", z)
    x, y = p.split(z)
    print(f"split({z}) ->", x, y)
    assert x, y == (a, b)
    g = p.generate()
    for i in range(0, a * b):
        a, b = (next(g), p.split(i))
        print(i, a, b)
        assert a == b