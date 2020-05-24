# Write a code to find the sum of numbers divisible by 4.The code must allow the
# user to accept a number and add it to the sum if it is divisible by 4. It should
# continue accepting numbers as long as the user wants to provide an input and
# should display the final sum.

def sum_of_numbers_divisable_by_4():

    print("You can enter a number as long as you want. Otherwise press q to quite")
    num = 0
    
    while True:

        number = input("Enter the number: ")
        
        if number != "q":
            number = int(number)
            if number%4 == 0:
                num = num + number
                
        elif number == "q":
            print(f"The sum of the number(s) which is divisable by 4 is {num}")
            break

sum_of_numbers_divisable_by_4()

    

    
