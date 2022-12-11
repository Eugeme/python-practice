def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))
def decomp(num):
    while num:
        yield num % 10
        num = num // 10
def rolldice_sum_prob(sum_, dice_amount):
    if sum_ > 6 * dice_amount:
        return 0
    lst = [i for i in range(int('1' * dice_amount), 6 * int('1' * dice_amount) + 1)]
    lst = [n for n in lst if all(6 >= x > 0 for x in decomp(n))]
    count = 0
    for i in lst:
        if sumDigits(i) == sum_:
            count += 1
    return count / 6 ** dice_amount