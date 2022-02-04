# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
#
# For each word:
#
# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# Note: there are no special characters used, only letters and spaces
#
# Examples
# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'

def decipher_this(string):
    string1 = string
    for i in string1:
        if i in ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            string1 = string1.replace(i, '')
    string1 = string1.split()
    for i in string1:
        if i in string:
            string = string.replace(i, chr(int(i)))
    string = string.split()

    result = []
    for i in string:
        if len(i) < 3:
            result.append(i)
        if len(i) >= 3:
            result.append(i[0] + i[-1] + i[2:-1] + i[1])
    res = ''
    for i in result:
        res = res + ' ' + i

    return res[1:]
