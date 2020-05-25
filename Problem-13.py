# Write a python function to check whether three given numbers can form the sides of a
# triangle.
# Hint
# : Three numbers can be the sides of a triangle if none of the numbers are greater than or equal
# to the sum of the other two numbers.


def triangle(side1, side2, side3):
    if side1 > (side2 + side3) and side2 > (side1 + side3) and side3 > (side1 + side2):
        return "valid"
    else:
        return "invalid"



if __name__ == "__main__":
    side1 = int(input("Enter the first side of the triangle: "))
    side2 = int(input("Enter the second side of the triangle: "))
    side3 = int(input("Enter the third side of the triangle: "))

    Valid_triangle = triangle(side1, side2, side3)

    print(f"This triangle is {Valid_triangle}")