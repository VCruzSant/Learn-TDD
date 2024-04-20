# 1 - receive a number

# 2 - is the number multiple of 3 or 5 ?:
# Multiple 3 and 5!

# 3 - is the number multiple of 3:
# Multiple 3!

# 4 - is the number multiple of 5:
# Multiple 5!

# 4 - isn`t multiple of 3 or 5:
# Fail!

def is_multiple_3_5(n):
    assert isinstance(n, int), 'N must be Int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Multiple 3 and 5!'

    if n % 3 == 0:
        return 'Multiple 3!'

    if n % 5 == 0:
        return 'Multiple 5!'

    return "Fail!"
