"""
def test():
    n = 0
    while n < 3:
        yield n
        n += 1

g = test()

print(g.__next__())

print(g.__next__())

print(g.__next__())
"""

def test_2():
    n = 0
    while n < 3:
        print(n)
        print("before yield")
        x = yield n
        print("after yield")
        if x is not None:
            print(x)
        else:
            print("x not exist")
        n += 1
        print(n)

g2 = test_2()


print("\n---------------\n")
print(g2.__next__())


print("\n---------------\n")
g2.send(123)

print("\n---------------\n")
print(g2.__next__())