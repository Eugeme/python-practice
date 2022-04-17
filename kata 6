#Write a function that calculates the least common multiple of its arguments;
#each argument is assumed to be a non-negative integer. 
#In the case that there are no arguments return 1.

def check(a, b):
    for i in a:
        if b % i != 0:
            return True

def lcm(*args):
    if 0 in args: return 0
    if len(args) == 0: return 1
    f = list(args)[-1]
    count = 2
    while check(args, f):
        f = list(args)[-1] * count
        count += 1
    return f


print(lcm(20, 1, 6, 10, 3, 7, 8, 4))
