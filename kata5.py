# Input is a string, for example "5x^4". The function f(x) consists of a single term only. Variable is denoted by x.
# Output should be a string, for example "20x^3".
# Examples
# "3x^2"  => "6x"
# "-5x^3" => "-15x^2"
# "6x^-2" => "-12x^-3"
# "5x"    => "5"
# "-x"    => "-1"
# "42"    => "0"
def differentiate(poly):
    if poly == 'x': return '1'
    elif poly == '-x': return '-1'
    if poly[0] == '-' and poly[1:].isdigit() == True or poly.isdigit() == True:
        return str(0)
    elif poly[-1] == 'x':
        return poly[:-1]
    else:
        degree = ''
        end = 0
        b = poly[::-1]
        for i in range(len(b)):
            if b[i] == '^':
                end += i
                break
            degree += b[i]
        degree = degree[::-1]
        coef = ''
        for i in range(len(poly)):
            if poly[i] == 'x':
                end += i
                break
            coef += poly[i]
        if coef == '-':
            res = str(-int(degree)) + poly[1:-len(degree)] + str(int(degree) - 1)
            if res[:-3:-1] == '1^':
                return res[:-2]
            return res
        elif coef == '':
            res = str(int(degree)) + poly[:-len(degree)] + str(int(degree) - 1)
            if res[:-3:-1] == '1^':
                return res[:-2]
            return res
        res = str(int(coef)*int(degree)) + poly[len(coef):-len(degree)]+str(int(degree)-1)
        if res[:-3:-1] == '1^':
            return res[:-2]
        return res


a = '12345'
print(a[:-3:-1])








