# Write a function, check_palindrome() to check whether the given string is a palindrome or
# not. The function should return true if it is a palindrome else it should return false.

def check_palindrome(string):

    string1 = string[:]
    string1 = string1[::-1]
    if string == string1:
        return "true"
    else:
        return "false"

if __name__ == "__main__":
    string = input("Enter here to check whether the string is a palindrome or not:  ")
    check = check_palindrome(string)
    print(check)