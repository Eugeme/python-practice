# A stream of data is received and needs to be reversed.
# Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:
# 11111111000000000000111110101010
# should become:
# 10101010000011110000000011111111
# The total number of bits will always be a multiple of 8.
# The data is given in an array as such:
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]


def data_reverse(data):
    len_data = int(len(data) / 8)
    lst = ''
    bits = 8
    count = 0
    while len_data != 0:
        while count != bits:
            lst += str(data[count])
            count += 1
        bits += 8
        lst += ' '
        len_data -= 1
    lst = list(reversed(lst.split(' ')))
    lst.remove('')
    result = []
    for i in range(len(lst)):
        for x in range(len(lst[i])):
            result.append(int(lst[i][x]))
    return result


print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))
