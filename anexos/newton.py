# Implementação do método de Newton para calcular raiz quadrada baseada no
# livro _Structure and Interpretation of Computer Programs


def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(
            improve(guess, x), x
        )  # chamada recursiva à função, usando palpites melhorados


def good_enough(guess, x):
    return abs((guess * guess) - x) < 0.001


def improve(guess, x):
    return average(guess, x / guess)


def average(x, y):
    return (x + y) / 2


# Abstrai a chamada da função sqrt_iter
def sqrt(x):
    return sqrt_iter(1.0, x)  # usamos 1.0 como palpite inicial da raiz quadrada de x


print(sqrt(2.0))
