BASE_62_VALUES = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def to_base(num, base = 62):
    if num == 0:
        return a[0]
    result = ''
    while (num > 0):
        r = num % base
        result = result + BASE_62_VALUES[r]
        num = (num//base)
    return result

def from_base(value, base = 62):
    base_10_num = 0
    digit = 0
    value = list(value)
    for i in value.reverse():
        num = BASE_62_VALUES.index(i)
        base_10_num += num * (base ** digit)
        digit += 1
    return base_10_num