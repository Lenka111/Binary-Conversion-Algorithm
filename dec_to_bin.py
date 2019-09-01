# Elena Voinu
# binary representation as a string, and it handles all integers, not just positive ones.


def binary_rep(n):

    if n == 0:
        return '0'
    else:

        k = abs(n)
        s = ' '
        while k > 0:
            s = str(k % 2) + s
            k = k // 2

        if n < 0:
            s = '- ' + s
        return s


print(binary_rep(-2))












