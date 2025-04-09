import cvc5
from cvc5 import Kind

if __name__ == "__main__":
    tm = cvc5.TermManager()
    slv = cvc5.Solver(tm)

    slv.setOption("produce-models", "true")
    slv.setLogic("LIA")

    intSort = tm.getIntegerSort()
    x = tm.mkVar(intSort, "x")
    y = tm.mkVar(intSort, "y")

    xMinusY = tm.mkTerm(Kind.SUB, x, y)
    minus = slv.defineFun("minus", [x, y], intSort, xMinusY, True)

    five = tm.mkInteger(5)
    ten = tm.mkInteger(10)

    app = tm.mkTerm(Kind.APPLY_UF, minus, *[ten, five])
    slv.assertFormula(tm.mkTerm(Kind.GEQ, app, five))
    print(slv.checkSat())
