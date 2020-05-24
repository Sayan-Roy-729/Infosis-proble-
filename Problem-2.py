# Write a code to check whether a given number is a palindrome.

def palindrome(number):

    '''It is a function to check a number whether it is palindrome or not.
    It takes only the number.
    Author: Sayan Roy
    Date: 24th May 2020'''

    number1 = number[:]
    number1 = number1[::-1]

    if number == number1:
        print(f"The number {number} is palindrome")
    else:
        print(f"The number {number} is not palindrome")

if __name__ == "__main__":
    
    number = input("Enter the number to check whether it is palindrome or not: ")

    palindrome(number)


