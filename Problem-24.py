#  Write a python function, create_largest_number(), which accepts a list of numbers and
# returns the largest number possible by concatenating the list of numbers.
# Note: Assume that all the numbers are two digit numbers.


def create_largest_number(list_of_numbers):

    list_of_numbers.sort(reverse = True)
    largest_number = ""
    for numbers in list_of_numbers:
        largest_number = largest_number + str(numbers)
    return largest_number

if __name__ == "__main__":
    list_of_numbers = [23,34,55]
    print(create_largest_number(list_of_numbers))
    