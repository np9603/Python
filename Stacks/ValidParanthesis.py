
def ValidParanthesis(input):
    stack = []

    bracket_dict = {'(':')' , '[':']' , '{':'}'}

    for char in input:
        if char in ['(',')','{','}','[',']']:
            if char in bracket_dict:
                stack.append(bracket_dict[char])
            elif len(stack)==0 or char != stack.pop():
                return False
        else:
            continue
    return len(stack)==0




def main():

    print(ValidParanthesis(' ( ( ) ) '))
    print(ValidParanthesis('((()'))
    print(ValidParanthesis('([{'))

main()