# Write a Python program to generate the next 15 leap years starting from a given year.
# Populate the leap years into a list and display the list.

def leaapYear(year):

    list1 = []

    while len(list1) != 15:

        if year % 400 == 0:
            list1.append(year)
            year += 1
        elif year % 4 == 0:
            list1.append(year)
            year += 1
        else:
            year += 1
    
    print(list1)


if __name__ == "__main__":
    year = int(input("Enter a year to show next 15 leapyears: "))

    leaapYear(year)
