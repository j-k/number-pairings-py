from helpers import tn, tr
from test import tests

class Cantor:

    @staticmethod
    def join(x, y):
        return tn(x + y) + y

    @staticmethod
    def split(z):
        t = tr(z)
        return (
          (t * (t + 3) // 2) - z,
          z - ((t * (t + 1)) // 2)
        )

    @staticmethod
    def bounds():
      return (0, 0, 0)
    
    @staticmethod
    def generate():
        u, v = 0, 0
        while True:
            yield (u-v, v)
            if u == v:
                u += 1
                v = 0
            else:
                v += 1

if __name__ == "__main__":
    tests(Cantor)