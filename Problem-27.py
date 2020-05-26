# Write a recursive function, is_palindrome() to find out whether a string is a palindrome or
# not. The function should return true, if it is a palindrome. Else it should return false.
# Note- Perform case insensitive operations wherever necessary.


def is_palindrome(text):

    if len(text) <= 1:
        return True
    else:
        if text[0] == text[-1]:
            is_palindrome(text[1:-1])
        else:
            return False

if __name__ == "__main__":
    text = input("Enter the text to check where it is palindrome or not: ")
    print(is_palindrome(text))