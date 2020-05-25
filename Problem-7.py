# Write a python program that displays a message as follows for a given number:
# ● If it is a multiple of three, display "Zip"
# ● If it is a multiple of five, display "Zap".
# ● If it is a multiple of both three and five, display "Zoom".
# ● If it does not satisfy any of the above given conditions, display "Invalid".

def display_message(number):

    if number % 3 == 0 and number % 5 == 0:
        print("Zoom")

    elif number % 3 == 0:
        print("Zip")

    elif number % 5 == 0:
        print("Zap")

    else:
        print("Invalid")
    


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    display_message(number)
