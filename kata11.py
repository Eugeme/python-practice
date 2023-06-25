# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def expand(expression):
    if '^0' in expression:
        return '1'

    caret = expression.find('^')
    power = int(expression[caret+1:])

    variable = expression.translate({ord(i): None for i in '()+-1234567890^'})

    a = expression[:expression.find(variable)+1].replace(f'(-{variable}', '-1')
    a = a.replace(f'({variable}', '1')
    a = a.translate({ord(i): None for i in f'({variable}'})
    a = int(a)

    b = int(expression[expression.find(variable)+1:expression.find(')'):])
    if b == 0:
        return (str(a) if a != 1 else '') + f'{variable}^{power}'

    result = ''

    for i in range(power):
        binomial_coefficient = int(factorial(power)/(factorial(i) * factorial(power-i)))
        result += str(binomial_coefficient * a**(power-i) * b**i) + f'{variable}^{power-i}+'

    if result.startswith(f'1{variable}'):
        result = result[1:]
    elif result.startswith(f'-1{variable}'):
        result = '-' + result[2:]

    result = result.replace('^1+', '+')

    result += str(b ** power)

    result = result.replace('+-', '-')

    return result


print("(x+1)^2        =>    ", expand("(x+1)^2"))
print("(p-1)^3        =>    ", expand("(p-1)^3"))
print("(2f+4)^6       =>    ", expand("(2f+4)^6"))
print("(-2a-4)^0      =>    ", expand("(-2a-4)^0"))
print("(-12t+43)^2    =>    ", expand("(-12t+43)^2"))
print("(r+0)^203      =>    ", expand("(r+0)^203"))
print("(-x-1)^2       =>    ", expand("(-x-1)^2"))
print("(-c+18)^3      =>    ", expand("(-c+18)^3"))
