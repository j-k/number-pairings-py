def tests(pairing, a = 10, b = 34):
    p = pairing()
    z = p.join(a, b)
    print(f"join({a}, {b}) ->", z)
    x, y = p.split(z)
    print(f"split({z}) ->", x, y)
    assert x, y == (a, b)
    g = pairing.generate()
    for i in range(0, 10):
        a, b = (next(g), p.split(i))
        print(i, a, b)
        assert a == b

if __name__ == "__main__":
    tests()