def baseConverter(decimalnumber,base):

    digits = '0123456789ABCDEF'
    stack = []

    while decimalnumber > 0:
        remainder = decimalnumber % base
        stack.append(remainder)
        decimalnumber = decimalnumber // base

    ans = ''
    while len(stack) > 0:
        ans += str(stack.pop())

    return ans


def main():
    print(baseConverter(25,8))
    print(baseConverter(256,16))
    print(baseConverter(10,2))
    print(baseConverter(26,26))


main()