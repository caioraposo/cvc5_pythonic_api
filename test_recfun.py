from cvc5_pythonic_api import *

s = Solver()
n = Int("n")
r = Int("r")
fact = Function("fact", IntSort(), IntSort())
#fact = DefRecFunction(fact, [n], If(n == 0, 1, n * fact(n - 1)))
DefRecFunction(fact, [n], r)

#DefFunction(fact, [n], IntSort(), n + 1)

x = Int("x")
s.add(fact(x) == 100)
print(s.check())
m = s.model()
print(f"x: {m[x]}")
print(f"x: {m[fact]}")
print(m.evaluate(fact(10)))
