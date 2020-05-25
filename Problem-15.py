def function(num1,num2):
    l1 = []

    if int(num1) < int(num2):
        num2 = int(num2)
        num2 = num2 + 1
        for i in range(num2):
            k = str(i)
            j = 0
            for m in k:
                j = j + int(k)
            if j % 3 == 0:
                if int(i) % 5 == 0:
                    if num2 >= 10 and num2 <= 99:
                        l1.append(i)
    if len(l1) == 0:
        print("-1")
    else:
        print("The list is ", l1)
        maximum = max(l1)
        print("Mamimum elemen - ", maximum)

if __name__ == "__main__":
                
    num1 = input("Enter the 1st number: ")
    num2 = input("Enter the 2nd number: ")

    function(num1,num2)