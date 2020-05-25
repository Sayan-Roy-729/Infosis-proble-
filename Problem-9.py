def product(num1, num2, num3):

    if num2 == 7:
        print(f"The product is {num3}")
    
    elif num3 == 7:
        print("The product is -1")

    elif num1 == 7:
        product = num2 * num3
        print(f"The product is {product}")
    
    else:
        product = num1 * num2 * num3
        print(f"The product is {product}")
    


if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    product(num1, num2, num3)