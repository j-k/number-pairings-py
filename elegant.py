import isqrt.isqrt as isqrt
from test import tests

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
      if t < sq_z: return (sq_z, t)
      else: return (t - sq_z, sq_z)
    
    @staticmethod
    def bounds():
        return (0, 0, 0)
    
    @staticmethod
    def generate():
        u, v, w = 0, 0, 0
        while True:
            yield (u, v)
            if u == w and v < w:
                if v < w-1: v += 1
                else: u, v = 0, w
            elif u < w and v == w:
                u += 1
            elif u == w and v == w:
                u, v, w = (u+1, 0, w+1)
            else: assert False

if __name__ == "__main__":
    tests(Elegant)