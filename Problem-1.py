#  Write a code to find the minimum among three given numbers.


def minThreeNumber(num1, num2, num3):

    '''It is a function to find out of the minimun number amon the three numbers. It takes three numbers.
    And print that number which is smallest.'''
    

    if num1<num2 and num1<num3:
        print(f"The minimum number among {num1}, {num2}, {num3} is {num1}")
    elif num2<num1 and num2<num3:
        print(f"The minimum number among {num1}, {num2}, {num3} is {num2}")
    elif num3<num1 and num3<num2:
        print(f"The minimum number among {num1}, {num2}, {num3} is {num3}")
    else:
        print("Some error occured")

if __name__ == "__main__":
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    num3 = int(input("Enter the 3rd number: "))

    minThreeNumber(num1, num2, num3)

    