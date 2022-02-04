# Take 2 strings s1 and s2 including only letters from ato z.
# Return a new sorted string, the longest possible, containing distinct
# letters - each taken only once - coming from s1 or s2.
# Example:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"


def longest(a1, a2):
    print(a1, a2)
    a3 = []
    if len(a1) > len(a2):
        for i in a1:
            for j in a2:
                if i == j:
                    a1 = a1.replace(i, '')
        a3 += a1
        a3 += a2
    elif len(a1) < len(a2) or len(a1) == len(a2):
        for i in a2:
            for j in a1:
                if i == j:
                    a2 = a2.replace(i, '')
        a3 += a2
        a3 += a1

    a3 = list(set(a3))
    a3 = sorted(a3)
    a4 = ''
    for i in a3:
        a4 += i
    return str(a4)
