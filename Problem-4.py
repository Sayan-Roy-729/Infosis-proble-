#  A three digit number is said to be an “Armstrong number” if the sum of the
# third power of its individual digits is equal to the number itself.Write a program
# to check whether a number is armstrong or not.



def armstrong(number):
    sum  = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10


    if number == sum:
        return "armstrong"
    else:
        return "not armstrong"


if __name__ == "__main__":
    number = int(input("Enter the three digit number: "))

    check = armstrong(number)
    print(f"The number {number}, you have entered is {check} number")