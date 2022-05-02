def solve(eq: str):
    eq = eq.replace(' ', '')
    a = eq.find('x') < eq.find('=') and eq[eq.find('x')-1] != '-' or eq.find('x') > eq.find('=') and eq[eq.find('x')-1] == '-'
    eq = eq.replace('x', '0')
    left_sight = eq[:eq.find('=')]
    right_sight = eq[eq.find('=')+1:]
    res = eval(left_sight) - eval(right_sight)
    if a:
        return -res
    return res
