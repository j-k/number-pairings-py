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
            return (z // self.s, z % self.s)
        else:
            return (z % self.s, z // self.s)

    def bounds(self):
        if self.xy == 0:
            return (0, self.s, 0)
        else:
            return (self.s, 0, 0)

    def generate(self):
        def _generate_x(s=self.s):
            u, v = 0, 0
            while True:
                yield u, v
                if v < s - 1: v += 1
                else: u += 1; v = 0
        def _generate_y(s=self.s):
            u, v = 0, 0
            while True:
                yield u, v
                if u < s - 1: u += 1
                else: v += 1; u = 0
        if self.xy == 0: return _generate_x()
        else: return _generate_y()

if __name__ == "__main__":
    p = Stack(6, 1)
    a, b = 2, 3
    z = p.join(a, b)
    print(f"join({a}, {b}) ->", z)
    x, y = p.split(z)
    print(f"split({z}) ->", x, y)
    assert x, y == (a, b)
    g = p.generate()
    for i in range(0, 10):
        a, b = (next(g), p.split(i))
        print(i, a, b)
        #assert a == b