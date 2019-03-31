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
