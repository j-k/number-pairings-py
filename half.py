from helpers import tn, tr, ext
from test import tests

# half pairing (only x <= y pairs)

class Half:

    @staticmethod
    def join(x, y): return tn(max(x, y)) + min(x, y)
    
    @staticmethod
    def split(z): return (ext( z ), tr( z ))
    
    @staticmethod
    def bounds(): return (0, 0, 0)

    @staticmethod
    def generate():
        u, v = 0, 0
        while True:
            yield (u, v)
            if u == v:
                v += 1
                u = 0
            else:
                u += 1

if __name__ == "__main__":
    tests(Half)