# Implementação do método de Newton para calcular raiz quadrada baseada no
# livro _Structure and Interpretation of Computer Programs

def good_enough(guess, x):
    return abs((guess * guess) - x) < 0.001

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return average(guess, x / guess)

def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def sqrt(x):
    return sqrt_iter(1.0, x)

print(sqrt(2))
