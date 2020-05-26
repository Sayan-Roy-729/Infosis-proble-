# Write a python function, check_double(number) which accepts a whole number and returns
# True if it satisfies the given conditions.

# 1. The number and its double should have exactly the same number of digits.
# 2. Both the numbers should have the same digits ,but in different order.
# Otherwise it should return False.

# Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but
# in a different order.


def check_double(number):

    double_number = number * 2

    number = str(number)
    double_number = str(double_number)
    list1 = []
    if len(number) == len(double_number):
        for digits in number:
            for j in double_number:
                if digits == j:
                    list1.append(j)
        if len(list1) == len(number):
            return True
        else:
            return False   
    else:
        return False

if __name__ == "__main__":
    number = int(input("Enter the number here: "))
    print(check_double(number))
        

            

