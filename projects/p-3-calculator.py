# normal calculator

def calculator(a, op, b):
    if op == "+":
        resultssum = a + b
        return resultssum
    elif op == "-":
        resultsdif = a - b
        return resultsdif
    elif op == "*":
        resultspro = a * b
        return resultspro
    elif op == "/":
        if b == 0:
            err = "divide by 0 is not allowed"
            return err
        else:
            resultsquo = a / b
            return resultsquo
    else:
        wrongformated = "number or operator is invalid"
        return wrongformated

resultscal1 = calculator(1, "+", 4)
resultscal2 = calculator(1, "-", 4)
resultscal3 = calculator(1, "*", 4)
resultscal4 = calculator(1, "/", 4)
resultscal5 = calculator(1, "/", 0)
print(resultscal1, resultscal2, resultscal3, resultscal4, resultscal5)