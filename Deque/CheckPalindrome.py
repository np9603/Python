from Deque import Deque

def checkPalindrome(input):

    deq = Deque()

    for char in input:
        deq.addFront(char)

    balanced = True

    while deq.size() > 1 and balanced == True:
        first_character = deq.removeFront()
        last_character = deq.removeRear()
        if first_character != last_character:
            return False
    return True

def main():

    print(checkPalindrome("radar"))
    print(checkPalindrome("madam"))
    print(checkPalindrome("aba"))
    print(checkPalindrome("abc"))
main()