from cvc5_pythonic_api import *

s = Solver()
fact = RecFuction("fact", IntSort())
n, m = Ints("n m")
DefRecFunction(fact, [n, m], If(n == 0, 1, n * fact(n - 1, m)))

s.add()

print(s.check())
m = s.model()
print(f"fact: {m[fact]}")
print(m.evaluate(fact(5, 10)))

# TODOS:
# 1. Add RecFunction, use mkConst
# 2. Reproduce example using mkConst and then DefRecFunction.
# 3. Take a look at declareConst.
