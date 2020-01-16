def decimalToBinary(decimalnumber):
    stack = []

    while decimalnumber > 0:
        remainder = decimalnumber % 2
        stack.append(remainder)
        decimalnumber = decimalnumber // 2
    ans = ''
    while len(stack) > 0:
        ans = ans + str(stack.pop())

    return ans

def main():
    print(decimalToBinary(10))
    print(decimalToBinary(12))
    print(decimalToBinary(15))
    print(decimalToBinary(16))


main()